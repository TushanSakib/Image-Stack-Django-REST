from django.urls import path,include
from . import views
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'snippet',SnippetViewSet,basename='snippet')
urlpatterns = router.urls

urlpatterns = [
    path('api/',include(router.urls)),
    path('',views.login_user,name="login_user"),
    path('logout_user/',views.logout_user,name="logout_user"),
    path('register_user/',views.register_user,name="register_user"),
    path('search_snippet/',views.search_snippet,name="search_snippet"),

    path('home/',HomeView.as_view(),name="home"),
    path('add_snippet/',SnippetAdd.as_view(),name="add_snippet"),
    path('update_snippet/<int:pk>',SnippetUpdate.as_view(),name='update_snippet'),
    path('delete_snippet/<int:pk>',SnippetDelete.as_view(),name='delete_snippet'),
    path('details_snippet/<int:pk>',SnippetDetailsView.as_view(),name='details_snippet'),
]