import json

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.status import HTTP_200_OK

from posts.models import Like, Post, Dislike


# Create your views here.
@csrf_exempt
@api_view(["GET"])
# this view to view all posts and likescount for each post
def post_data(request):
    obj = Post.objects.values("id", "description", "likes", "date_posted")
    print("obj", obj)

    obj = list(obj)
    print("obj", obj)

    data = obj
    print("data1", data)
    return Response(data, status=HTTP_200_OK)


@csrf_exempt

@api_view(["POST"])
# this view to like or unlike a post according to id
def like_post(request, id):
    like_post = Post.objects.get(id=id)
    if like_post.likes.filter(id=request.user.id).exists():
        like_post.likes.remove(request.user)
        dislike_author = request.user
        dislike = Dislike.objects.create(
            dislike_post=like_post,
            dislike_author=dislike_author
        )
        dislike.save()
    else:
        like_post.likes.add(request.user)
        like_author = request.user
        like = Like.objects.create(
            like_post=like_post,
            like_author=like_author
        )
        like.save()
        data = {'Response': "success"}

        return Response(data, status=HTTP_200_OK)
    return Response({"success": "success"})


@csrf_exempt
@api_view(["GET"])
# this view to get list of users who liked apost according to post id
def like_users(request, id):
    like_post = Post.objects.get(id=id)
    like_users = like_post.likes.values("username", "email")

    obj = list(like_users)
    print("obj", obj)

    data = obj
    print("data1", data)
    return Response(data, status=HTTP_200_OK)
