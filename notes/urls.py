from django.urls import path
from .views import index,create,delete,update,about
from . import auth

urlpatterns=[
    path("",index,name="index"),
    path("create/",create,name="create"),
    path("delete/<int:pk>/",delete,name="delete"),
    path("update/<int:pk>/",update,name="update"),
    path("about/",about,name="about"),
    path("login/",auth.login,name="login"),
]