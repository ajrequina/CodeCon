from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.contrib.staticfiles.templatetags.staticfiles import static


class Profile(models.Model):
    owner = models.OneToOneField(User, related_name="my_profile")
    profile_photo = models.FileField(upload_to="profile_photos/%Y/%m/%d/", blank=True)
    cover_photo = models.FileField(upload_to="cover_photos/%Y/%m/%d/", blank=True)

    @property
    def profile_photo_url(self):
        if self.profile_photo:
            return self.profile_photo.url

        return (static('images/default.png'))

    @property
    def cover_photo_url(self):
        if self.cover_photo:
            return self.cover_photo.url
        return (static('images/cover.png'))

    def __unicode__(self):
        name = self.owner.first_name + " " + self.owner.last_name
        ucode = ""
        if name == " ":
            ucode = ucode + "@" + self.owner.username
        else:
            ucode = ucode + name + " (@" + self.owner.username + ")"

        return ucode


class Follow(models.Model):
    follower = models.ForeignKey(User, related_name="followed")
    followed = models.ForeignKey(User, related_name="followers")
