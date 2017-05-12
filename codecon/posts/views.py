# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
import datetime
from django.contrib.auth.decorators import login_required

from posts.models import Post, Like, Comment

@login_required
def home_page(request):
    return render(request, 'home.html', {})

@login_required
def add_post_page(request):
    return render(request, 'addpost.html', {})

@login_required
def update_post_page(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        "post" : post
    }
    return render(request, 'editpost.html', context=context)

@login_required
def view_posts(request):
    posts = Post.objects.filter(owner=request.user)
    blogposts = []
    for post in posts:
        comments = Comment.objects.filter(commented_post=post)
        for item in comments:
            if item.owner == request.user:
                item.is_owner = True
            else:
                item.is_owner = False

        post.all_comments = comments
        post.all_likes = Like.objects.filter(liked_post=post)

    context = {
        "posts" : posts
    }

    return render(request, 'viewposts.html', context=context)

@login_required
def add_post(request):
    if request.method == "POST":
        title = request.POST.get('post_title')
        category = request.POST.get('post_category')
        owner = request.user
        language = request.POST.get('post_language')
        content = request.POST.get('post_content')

        Post.objects.create(title=title, category=category, owner=owner, language=language, content=content, date_created=datetime.datetime.now())
        return redirect("posts:view_posts")

@login_required
def update_post(request, pk):
    if request.method == "POST":
        instance = Post.objects.get(pk=pk)
        instance.title = request.POST.get('post_title')
        instance.category = request.POST.get('post_category')
        instance.language = request.POST.get('post_language')
        instance.content = request.POST.get('post_content')

        instance.save()

        return redirect("posts:post_detail", pk=pk)

@login_required
def delete_post(request, pk):
    if request.method == "GET":
        instance = Post.objects.get(pk=pk)
        print(instance)
        instance.delete()

    return redirect("posts:view_posts")

@login_required
def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(commented_post=post)
    for item in comments:
        if item.owner == request.user:
            item.is_owner = True
        else:
            item.is_owner = False

    post.all_comments = comments
    post.all_likes = Like.objects.filter(liked_post=post)

    if post.owner == request.user:
        post.is_owner = True
    else:
        post.is_owner = False

    context = {
        "post" : post
    }

    return render(request, 'post.html', context=context)

@login_required
def like_post(request, pk):
    post = Post.objects.get(pk=pk)
    if len(Like.objects.filter(liker=request.user, liked_post=post)) == 0:
        Like.objects.create(liker=request.user, liked_post=post)
    else:
        instance = Like.objects.get(liker=request.user, liked_post=post)
        instance.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def add_comment_detail(request, pk):
    post = Post.objects.get(pk=pk)
    content = request.POST.get("comment_content")
    owner = request.user
    Comment.objects.create(content=content, commented_post=post, owner=owner)
    return redirect('posts:post_detail', pk=pk)

@login_required
def add_comment_all(request, pk):
    post = Post.objects.get(pk=pk)
    content = request.POST.get("comment_content")
    owner = request.user
    Comment.objects.create(content=content, commented_post=post, owner=owner)
    return redirect('posts:view_posts')

@login_required
def delete_comment(request, pk):
    instance = Comment.objects.get(pk=pk)
    instance.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))




