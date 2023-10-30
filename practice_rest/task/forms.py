from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class ListItem(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = '__all__'
        labels={
            'name':'Name',
            'details':'Details',
            'due_date':'Due-Date',
            'snippet_image':'',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'details': forms.Textarea(attrs={'class':'form-control'}),
            'due_date':forms.DateTimeInput(attrs={'class':'form-control','placeholder':'YYYY-MM-DD'})
        }
class SnippetMore(forms.ModelForm):
    class Meta:
        model = SnippetImage
        fields = ['image']
        labels={
            'image':'',
        }

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
    address = forms.CharField(max_length=80,widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','address','password1','password2')

    def __init__(self,*args,**kwargs):
        super(RegisterUserForm,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'