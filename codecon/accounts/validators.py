from django.contrib.auth.models import User


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

