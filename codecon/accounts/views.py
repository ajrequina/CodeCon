# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def account_form(request):
    return render(request, 'account.html', {})

def logout_user(request):
    logout(request)
    return redirect('/home')

def login_user(request):
    username = request.POST.get('login_username')
    password = request.POST.get('login_password')
    error = ""
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect('/home/')
    if not username:
    	username = ""
    return render(request, 'account.html', {"error": error, "login_username" : username })

def register_user(request):
	if request.method == "POST":
		username = request.POST.get('reg_username')
		email = request.POST.get('reg_email')
		first_name = request.POST.get('reg_first_name')
		last_name = request.POST.get('reg_last_name')
		password1 = request.POST.get('reg_password1')
		password2 = request.POST.get('reg_password2')

		


def check_reg_fields(username, email, first_name, last_name, password1, password2):
	errors = []
	if not username:
		errors.append("Username is required.")
	else:
		if len(username) < 8:
			errors.append("Username must be at least 8 characters.")
	if not email:
		errors.append("Email is required.")
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


def create_user(data):
	pass

