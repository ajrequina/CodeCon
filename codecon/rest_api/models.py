from __future__ import unicode_literals
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
	if created:
		Token.objects.create(user=instance)
	
class Post(models.Model):
	title = models.CharField(max_length=100, blank=False)
	content = models.TextField(default="")
	created = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE, null=False)
