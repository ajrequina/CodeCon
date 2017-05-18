from __future__ import unicode_literals
import datetime

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from posts.models import Post, Like
from posts.factories import post_factory
from posts.forms import PostForm

from comments.models import Comment


@login_required
def add(request):
    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.owner = request.user
            post.date_created = date_created=datetime.datetime.now()
            post.save()

    next_url = request.GET.get("next", "")
    return redirect(next_url)


@login_required
def update(request, pk):
    if request.method == "POST":
        post = Post.objects.get(pk=pk)
        form = PostForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            post.title = data['title']
            post.content = data['content']
            post.language = data['language']
            post.category = data['category']
            post.save()

        return redirect("posts:detail", pk=pk)

    elif request.method == "GET":
        post = Post.objects.get(pk=pk)
        context = {
            "post" : post
        }
        return render(request, 'editpost.html', context=context)


@login_required
def delete(request, pk):
    if request.method == "GET":
        instance = Post.objects.get(pk=pk)
        instance.delete()

    return HttpResponseRedirect(request.path)


@login_required
def detail(request, pk):
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
def list(request, profile="0"):
    posts = post_factory.list(request.user, profile)
    context = {
        "posts" : posts,
        "owner" : request.user
    }

    if profile == "0":
        return render(request, 'home.html', context=context)
    else:
        return render(request, 'profile.html', context=context)


@login_required
def like(request, post_id):
    post = Post.objects.get(pk=post_id)
    if len(Like.objects.filter(liker=request.user, liked_post=post)) == 0:
        Like.objects.create(liker=request.user, liked_post=post)
    else:
        instance = Like.objects.get(liker=request.user, liked_post=post)
        instance.delete()

    next_url = request.GET.get("next", "")
    return redirect(next_url)
