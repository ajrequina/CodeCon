# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def account_form(request):
	return render(request, 'account.html', {})

def logout_user(request):
	logout(request)
	return redirect('accounts:account_form')

def login_user(request):
	if request.user.is_authenticated():
		return redirect('posts:homepage')

	username = request.POST.get('login_username')
	password = request.POST.get('login_password')
	errors = check_login_fields(username=username, password=password)
	if len(errors) <= 0:
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return redirect('posts:homepage')
		else:
			errors.append("Incorrect password.")

	if not username:
		username = ""
	print(errors)
	context = {
		"login_username" : username,
		"login_errors" : errors
	}
	return render(request, 'account.html', context=context)

def register_user(request):
	username = request.POST.get('reg_username')
	email = request.POST.get('reg_email')
	first_name = request.POST.get('reg_firstname')
	last_name = request.POST.get('reg_lastname')
	password1 = request.POST.get('reg_password1')
	password2 = request.POST.get('reg_password2')
	errors = check_reg_fields(username, email, first_name, last_name, password1, password2)
	if len(errors) <= 0:
		user = User.objects.create(username=username, email=email, first_name=first_name, last_name=last_name)
		user.set_password(password1)
		user.save()
		login(request, user)
		return redirect('posts:homepage')
	else:
		if not username:
			username = ""
		if not email:
			email = ""
		if not first_name:
			first_name = ""
		if not last_name:
		   last_name = ""

		context = {
			"reg_username" : username,
			"reg_email" : email,
			"reg_firstname" : first_name,
			"reg_lastname" : last_name,
			"reg_errors" : errors
		}

		return render(request, 'account.html', context=context)

def check_login_fields(username, password):
	errors = []
	if not username:
		errors.append("Username is required.")
	if not password:
		errors.append("Password is required.")
	else:
		if User.objects.filter(username=username).count() <= 0:
			errors.append("User does not exists.")

	return errors


def check_reg_fields(username, email, first_name, last_name, password1, password2):
	errors = []
	if not username:
		errors.append("Username is required.")
	else:
		if len(username) < 8:
			errors.append("Username must be at least 8 characters.")
		elif User.objects.filter(username=username).count() > 0:
			errors.append("Username already exists.")
	if not email:
		errors.append("Email is required.")
	else:
		if User.objects.filter(email=email).count() > 0:
			errors.append("Email already exists.")
	if not first_name:
		errors.append("Firstname is required.")
	if not last_name:
		errors.append("Lastname is required.")
	if not password1:
		errors.append("Password is required.")
	if not password2:
		errors.append("Confirm password is required.")
	else:
		if len(password1) < 8:
			errors.append("Password must be at least 8 characters.")
		elif password1 != password2:
			errors.append("Passwords do not match.")
	return errors

