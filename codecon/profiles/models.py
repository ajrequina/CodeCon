from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    owner = models.OneToOneField(User, related_name="my_profile")
    profile_photo = models.FileField(upload_to="profile_photo_uploads/%Y/%m/%d/")
    cover_photo = models.FileField(upload_to="cover_photo_uploads/%Y/%m/%d/")


class Follow(models.Model):
    follower = models.ForeignKey(User, related_name="my_followers")
    followed = models.ForeignKey(User, related_name="my_followed")
