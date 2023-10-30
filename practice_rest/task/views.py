from django.shortcuts import render,redirect,get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SnippetSerializer
from .models import Snippet,SnippetImage
from rest_framework import viewsets
from django.urls import reverse_lazy,reverse
from django.views.generic import ListView,UpdateView,DeleteView,CreateView,DetailView
from .forms import ListItem,SnippetMore
from rest_framework import status
from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm
from django.contrib.auth import authenticate,login,logout
#from .forms import RegisterUserForm
# Create your views here.

class SnippetViewSet(viewsets.ModelViewSet):
    serializer_class = SnippetSerializer
    queryset = Snippet.objects.all()
    
    def list(self,request):
        search = request.GET.get('search')
        queryset = self.queryset
        if search:
            queryset = queryset.filter(name__startswith = search)
        
        serialize = SnippetSerializer(queryset,many=True)
        return Response({'status':200,'data':serialize.data}, status=status.HTTP_204_NO_CONTENT)



class HomeView(ListView):
        model = Snippet
        template_name = 'home.html'

        def get_context_data(self,*args ,**kwargs):
            list_item = Snippet.objects.all()
            context = super(HomeView,self).get_context_data(*args,**kwargs)
            context["list_item"] = list_item
            return context

def detail_view(request,id):
    snippet = get_object_or_404(Snippet,id=id)
    photos = SnippetImage.objects.filter(snippet = snippet)
    return render(request,'details_snippet.html',{'snippet':snippet,'photos':photos})






class SnippetAdd(CreateView):
        model = Snippet
        form_class = ListItem
        template_name='add_snippet.html'
        
        def get_context_data(self,*args,**kwargs):
            list_item = Snippet.objects.all()

            context = super(SnippetAdd,self).get_context_data(*args,**kwargs)
            context["list_item"] = list_item
            return context
        success_url = reverse_lazy('home')


class SnippetDetailsView(DetailView):
        model = Snippet
        template_name = 'details_snippet.html'
        def get_context_data(self,*args ,**kwargs):
            list_it = Snippet.objects.get(id=self.kwargs['pk'])
            context = super(SnippetDetailsView,self).get_context_data(*args,**kwargs)
            context["list_it"] = list_it
        # stuff = get_object_or_404(Snippet,id=self.kwargs['pk'])
            return context
        #success_url = reverse_lazy('home')
    

class SnippetUpdate(UpdateView):
        model = Snippet
        form_class = ListItem
        template_name = 'update_snippet.html'

        def get_context_data(self,*args ,**kwargs):
            list_item = Snippet.objects.all()
            context = super(SnippetUpdate,self).get_context_data(*args,**kwargs)
            context["list_item"] = list_item
            return context
        success_url = reverse_lazy('home')

class SnippetDelete(DeleteView):
        model = Snippet
        template_name='snippet_delete.html'
        success_url = reverse_lazy('home')


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.success(request,"There was an error login in try again")
            return redirect('login_user')
    else:
        return render(request,'login.html')

def logout_user(request):
    logout(request)
    messages.success(request, "You are logged out")
    return redirect('login_user')


def register_user(request, password1=None):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            user = authenticate(username=username,password1=password1)
            login(request,user)
            messages.success(request,"Registration successful")
            return redirect('login_user')
    else:
        form = RegisterUserForm()
    return render(request, 'register_user.html',{'form':form,})
    

def search_snippet(request):
    if request.method == "POST":
        searched = request.POST['searched']
        snippet = Snippet.objects.filter(name__contains = searched)
        return render(request,'search_snippet.html',{'searched':searched,'snippet':snippet})
    else:
        return render(request,'search_snippet.html')
    

       
    

