# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from accounts.validators import check_login_fields, check_reg_fields


#  HTML files
def account_form(request):
	if request.user.is_authenticated():
		return redirect('posts:list', page_type='stream')

	return render(request, 'account.html', {})


# Account Operations
def logout_user(request):
	logout(request)
	return redirect('accounts:account_form')


def login_user(request):
	if request.user.is_authenticated():
		return redirect('posts:list', page_type='stream')

	username = request.POST.get('login_username')
	password = request.POST.get('login_password')
	errors = check_login_fields(username=username, password=password)
	if len(errors) <= 0:
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return redirect('posts:list', page_type='stream')
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
		user = authenticate(username=username, password=password1)
		if user is not None:
			if user.is_active:
				login(request, user)
				return redirect('posts:list', page_type='stream')
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
