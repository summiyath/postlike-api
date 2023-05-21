from django.urls import path

from posts import views

urlpatterns = [
    path('posts/', views.post_data, name='posts'),
    path('likes/<int:id>', views.like_post, name='likes'),
    path('like_users/<int:id>', views.like_users, name='like_users'),

]
