from __future__ import unicode_literals
import datetime

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from posts.models import Post, Like
from posts.factories import post_factory
from posts.forms import PostForm

from comments.models import Comment

from profiles.models import Follow

import markdown
from mdx_gfm import GithubFlavoredMarkdownExtension


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
        post = get_object_or_404(Post, pk=pk)
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
        post = get_object_or_404(Post, pk=pk)
        context = {
            "post" : post
        }
        return render(request, 'editpost.html', context=context)


@login_required
def delete(request, pk):
    if request.method == "GET":
        instance = get_object_or_404(Post, pk=pk)
        instance.delete()

    return HttpResponseRedirect(request.path)


@login_required
def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(commented_post=post)
    for item in comments:
        if item.owner == request.user:
            item.is_owner = True
        else:
            item.is_owner = False

    post.all_comments = comments
    post.all_likes = Like.objects.filter(liked_post=post)
    post.content =  markdown.markdown(post.content,
                         extensions=[GithubFlavoredMarkdownExtension()])
    print(post.content)
    if post.owner == request.user:
        post.is_owner = True
    else:
        post.is_owner = False

    context = {
        "post" : post
    }

    return render(request, 'post.html', context=context)


@login_required
def list(request, page_type='stream', user_id=None):
    user = request.user
    if user_id:
        user = get_object_or_404(User, pk=user_id)
        posts = post_factory.list(user, "profile")
    else:
        posts = post_factory.list(user, "stream")

    if not user.first_name:
        user.first_name = "CodeCon"
    if not user.last_name:
        user.last_name = "Programmer"

    is_owned = False
    is_followed = True

    if user == request.user:
        is_owned = True

    try:
        Follow.objects.get(follower=request.user, followed=user)
    except Exception as e:
        is_followed = False


    context = {
        "posts" : posts,
        "owner" : user,
        "is_owned" : is_owned,
        "is_followed" : is_followed
    }

    if page_type == "stream":
        return render(request, 'home.html', context=context)
    else:
        return render(request, 'profile.html', context=context)


@login_required
def like(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if len(Like.objects.filter(liker=request.user, liked_post=post)) == 0:
        Like.objects.create(liker=request.user, liked_post=post)
    else:
        instance = Like.objects.get(liker=request.user, liked_post=post)
        instance.delete()

    next_url = request.GET.get("next", "")
    return redirect(next_url)


@login_required
def top10(request):
    posts = []
    num = 10
    curr_week = datetime.datetime.now().isocalendar()[1]
    print(curr_week)
    if Post.objects.all().count() <= 10:
        posts = Post.objects.all()
    else:
        while num > 0 and Post.objects.all().count() > 0:
            for post in Post.objects.all():
                post_week = post.date_created.date().isocalendar()[1]
                if post_week == curr_week:
                    if len(posts) < 10:
                        posts.append(post)

            curr_week -= 1
            num = 10 - len(posts)

    posts = sorted(posts, key=lambda t: t.get_score, reverse=True)
    return render(request, 'top10.html', {"top_posts" : posts})
