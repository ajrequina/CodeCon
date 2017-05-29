from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.models import User

from posts.models import Post



def search_page(request):
    query = request.POST.get("query")
    if query is None:
        query = ""


    users = User.objects.all()
    posts = Post.objects.all()

    q1 = Q(username__icontains=query) | Q(first_name__icontains=query) | \
         Q(last_name__icontains=query) | Q(email__icontains=query)

    q2 = Q(title__icontains=query) | Q(content__icontains=query) | \
         Q(category__icontains=query) | Q(language__icontains=query) | \
         Q(owner__username__icontains=query) | Q(owner__first_name__icontains=query) | \
         Q(owner__last_name__icontains=query) | Q(owner__email__icontains=query)

    users = users.filter(q1)
    posts = posts.filter(q2)

    context = {
        "query" : query,
        "users" : users,
        "posts" : posts
    }
    return render(request, 'search.html', context=context)
