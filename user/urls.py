from django.urls import path

from . import views

app_name = 'users'  # define app name

urlpatterns = [

    # this url is used when anyone login through api into the likeproject.
    path('login', views.login, name='login'),
    # this url is used for register through api into the likeproject.

    path('register', views.register, name='register'),

]
