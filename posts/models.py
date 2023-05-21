import datetime

from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify




class Post(models.Model):
    description = models.CharField(max_length=255, blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='post_like', blank=True)
    dislikes = models.ManyToManyField(User, related_name='post_dislike', blank=True)

    tags = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.description


class Like(models.Model):
    like_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    like_author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.like_post


class Dislike(models.Model):
    dislike_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    dislike_author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.dislike_post
