from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from comments.models import Comment

from posts.models import Post


@login_required
def add(request, post_id):
    print(request.POST)
    post = Post.objects.get(pk=post_id)
    content = request.POST.get("content")
    owner = request.user
    Comment.objects.create(content=content, commented_post=post, owner=owner)

    next_url = request.GET.get("next", "")
    return redirect(next_url)


@login_required
def delete(request, pk):
    instance = Comment.objects.get(pk=pk)
    instance.delete()

    next_url = request.GET.get("next", "")
    return redirect(next_url)


@login_required
def update(request, pk):
    instance = Comment.objects.get(pk=pk)
    instance.content = request.POST.get("content")
    instance.save()

    next_url = request.GET.get("next", "")
    return redirect(next_url)
