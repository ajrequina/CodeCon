from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect

from comments.models import Comment

from posts.models import Post


@login_required
def add(request, post_id):
    print(request.POST)
    post = get_object_or_404(Post, pk=post_id)
    content = request.POST.get("content")
    owner = request.user
    Comment.objects.create(content=content, commented_post=post, owner=owner)

    next_url = request.GET.get("next", "")
    return redirect(next_url)


@login_required
def delete(request, pk):
    instance =get_object_or_404(Comment, pk=pk)
    instance.delete()

    next_url = request.GET.get("next", "")
    return redirect(next_url)


@login_required
def update(request, pk):
    instance =get_object_or_404(Comment, pk=pk)
    instance.content = request.POST.get("content")
    instance.save()

    next_url = request.GET.get("next", "")
    return redirect(next_url)
