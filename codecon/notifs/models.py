from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Notification(models.Model):
    receiver = models.ForeignKey(User, related_name="notifs")
    description = models.TextField(default="")
    read_date = models.DateTimeField(null=True, blank=True)
    target_link = models.CharField(max_length=100, default="")
    page_type = models.CharField(max_length=200)
    create_date = models.DateTimeField(auto_now=True)
    actor = models.ForeignKey(User)


    class Meta:
        ordering = ['-create_date']

    def __str__(self):
        return self.description
