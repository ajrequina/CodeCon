# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
import datetime

from posts.models import Post, Like, Comment

def home_page(request):
    return render(request, 'home.html', {})

def add_post_page(request):
    return render(request, 'addpost.html', {})

def update_post_page(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        "post" : post
    }
    return render(request, 'editpost.html', context=context)

def view_posts(request):
    posts = Post.objects.filter(owner=request.user)
    blogposts = []
    for post in posts:
        post.all_comments = Comment.objects.filter(commented_post=post)
        post.all_likes = Like.objects.filter(liked_post=post)
    context = {
        "posts" : posts
    }

    return render(request, 'viewposts.html', context=context)

def add_post(request):
    if request.method == "POST":
        title = request.POST.get('post_title')
        category = request.POST.get('post_category')
        owner = request.user
        language = request.POST.get('post_language')
        content = request.POST.get('post_content')

        Post.objects.create(title=title, category=category, owner=owner, language=language, content=content, date_created=datetime.datetime.now())
        return redirect("posts:view_posts")

def update_post(request, pk):
    if request.method == "POST":
        instance = Post.objects.get(pk=pk)
        instance.title = request.POST.get('post_title')
        instance.category = request.POST.get('post_category')
        instance.language = request.POST.get('post_language')
        instance.content = request.POST.get('post_content')

        instance.save()

        return redirect("posts:post_detail", pk=pk)

def delete_post(request, pk):
    if request.method == "GET":
        instance = Post.objects.get(pk=pk)
        print(instance)
        instance.delete()

    return redirect("posts:view_posts")

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    post.all_comments = Comment.objects.filter(commented_post=post)
    post.all_likes = Like.objects.filter(liked_post=post)

    if post.owner == request.user:
        post.is_owner = True
    else:
        post.is_owner = False

    context = {
        "post" : post
    }

    return render(request, 'post.html', context=context)

def like_post(request, pk):
    post = Post.objects.get(pk=pk)
    if len(Like.objects.filter(liker=request.user, liked_post=post)) == 0:
        Like.objects.create(liker=request.user, liked_post=post)
    else:
        instance = Like.objects.get(liker=request.user, liked_post=post)
        instance.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))





