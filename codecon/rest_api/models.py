from __future__ import unicode_literals

from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import uuid

class AccountManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('User must have a valid email address.')

        if not password:
        	raise ValueError('User must have a password')

        if not kwargs.get('username'):
            raise ValueError('User must have a valid username.')

        if not kwargs.get('first_name'):
        	raise ValueError('User must have a firstname.')

        if not kwargs.get('last_name'):
        	raise ValueError('User must have a lastname.')

        account = self.model(
            email=self.normalize_email(email), username=kwargs.get('username'),
            first_name=kwargs.get('first_name'), last_name=kwargs.get('last_name'),
        )

        account.set_password(password)
        account.save()

        return account

    def create_superuser(self, email, password, **kwargs):
        account = self.create_user(email, password, **kwargs)

        account.is_admin = True
        account.save()

        return account

class Account(AbstractBaseUser):
	email = models.EmailField(unique=True)
	username = models.CharField(max_length=50, unique=True)
	first_name = models.CharField(max_length=100, blank=True)
	last_name = models.CharField(max_length=100, blank=True)
	is_admin = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = AccountManager()
	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS =['email', 'first_name', 'last_name']
	
	def __unicode__(self):
		return self.email
	def get_full_name(self):
		return ' '.join([self.first_name, self.middle_name, self.last_name])
	def get_short_name(self):
		return self.first_name
	def get_user_details(self):
		return {
    	  'first_name' : self.first_name,
    	  'last_name' : self.last_name,
    	  'email' : self.email,
    	  'username' : self.username
    	}

class User(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email = models.EmailField(unique=True)
	password = models.CharField(max_length=100)
	username = models.CharField(max_length=50, unique=True)
	security_token = models.UUIDField(default=uuid.uuid4)

	class Meta:
		db_table = "user"



