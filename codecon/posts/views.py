# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from posts.models import Post, Like, Comment

def home_page(request):
    return render(request, 'home.html', {})

def add_post_page(request):
    print("I AM HERE")
    return render(request, 'addpost.html', {})

def view_posts(request):
    posts = Post.objects.filter(owner=request.user)
    for post in posts:
        post.comments = Comment.objects.filter(commented_post=post)
        print(post.comments)
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

        Post.objects.create(title=title, category=category, owner=owner, language=language, content=content)
        posts = Post.objects.filter(owner=request.user)
        context = {
            "posts" : posts
        }

        return render(request, 'viewposts.html', context=context)

def view_post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        "post" : post
    }

    return render(request, 'post.html', context=context)

def like_post(request, pk):
    post = Post.objects.get(pk=pk)
    Like.objects.create(liker=request.user, liked_post=post)
    view_posts(request)


