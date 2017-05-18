from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage

from profiles.forms import ProfilePhotoForm, CoverPhotoForm, ProfileForm

@login_required
def settings_page(request):
    context =  {"user" : request.user}
    return render(request, 'settings.html', context=context)


@login_required
def change_info(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")

        user = User.objects.get(pk=request.user.pk)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        errors = []

        if len(errors) == 0:
            return redirect("posts:list", profile="1")
        else:
            context = {
                "info_errors" : errors
            }
            return render(request, 'settings.html', context=context)


@login_required
def change_credentials(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")

        errors = []
        if User.objects.filter(username=username).count() > 0:
            errors.append("Username already exists.")
        if User.objects.filter(email=email).count() > 0:
            errors.append("Email already exists.")

        if len(errors) == 0:
            user = User.objects.get(pk=request.user.pk)
            user.username = username
            user.email = email
            user.save()
            return redirect("posts:list", profile="1")
        else:
            context = {
                "credential_errors" : errors
            }
            return render(request, 'settings.html', context=context)


def change_password(request):
    if request.method == 'POST':
        new_password1 = request.POST.get("new_password1")
        new_password2 = request.POST.get("new_password2")
        old_password1 = request.POST.get("old_password1")

        user = User.objects.get(pk=request.user.pk)
        print(user.check_password(old_password1))
        return render(request, 'settings.html', {})

def change_profile_photo(request, pk):
    if request.method == 'POST':
        user = User.objects.get(pk=pk)
        owner = {"owner": user}
        form = ProfilePhotoForm(request.FILES, owner)
        if form.is_valid():
            form.save()
            return redirect('posts:homepage')


def change_cover_photo(request, pk):
    if request.method == 'POST':
        user = User.objects.get(pk=pk)
        owner = {"owner": user}
        form = CoverPhotoForm(request.FILES, owner)
        if form.is_valid():
            form.save()
            return redirect('posts:homepage')


def change_profile_photos(request, pk):
    if request.method == 'POST':
        user = User.objects.get(pk=pk)
        owner = {"owner": user}
        form = ProfileForm(request.FILES, owner)
        if form.is_valid():
            form.save()
            return redirect('posts:homepage')



