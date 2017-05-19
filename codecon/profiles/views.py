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

    return redirect("profiles:setting")


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

    return redirect("profiles:setting")

def change_password(request):
    if request.method == 'POST':
        new_password1 = request.POST.get("new_password1")
        new_password2 = request.POST.get("new_password2")
        old_password = request.POST.get("old_password")

        user = User.objects.get(pk=request.user.pk)
        errors = []
        if new_password1 == None or new_password2 == None or old_password == None:
            if new_password1 == None:
                errors.append("Enter your new password.")
            elif new_password2 == None:
                errors.append("Confirm your new password.")
            elif old_password == None:
                errors.append("Enter your old password.")
        else:
            if len(new_password1) < 8 or len(new_password2) < 8 or len(old_password) < 8:
                errors.append("Passwords must be at least 8 characters.")
            elif new_password1 != new_password2:
                errors.append("New passwords do not match.")
            elif not user.check_password(old_password):
                errors.append("Enter your correct old password.")

        if len(errors) == 0:
            user.set_password(new_password1)
            user.save()
            return redirect("accounts:logout")
        else:
            context = {
                "password_errors" : errors
            }

            return render(request, 'settings.html', context=context)

    return redirect("profiles:setting")

def change_profile_photo(request):
    if request.method == 'POST':
        user = User.objects.get(pk=request.user.pk)
        print(request.FILES)
        form = ProfilePhotoForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('posts:list', profile="1")

    return redirect("profiles:setting")


def change_cover_photo(request):
    if request.method == 'POST':
        user = User.objects.get(pk=request.user.pk)

        form = CoverPhotoForm(request.POST, request.FILES, instance=request.user)
        print("CHANGE COVER PHOTO")
        if form.is_valid():
            form.save()
            return redirect('posts:list', profile="1")

    return redirect("profiles:setting")


def change_profile_photos(request, pk):
    if request.method == 'POST':
        user = User.objects.get(pk=pk)
        owner = {"owner": user}
        form = ProfileForm(request.FILES, owner)
        if form.is_valid():
            form.save()
            return redirect('posts:homepage')



