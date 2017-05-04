from __future__ import unicode_literals
from django.contrib.auth.models import User
from rest_framework import viewsets 

from codecon_api.serializers import RegisterSerializer


class RegisterViewSet(viewsets.ModelViewSet):
	serializer_class = RegisterSerializer
	queryset = User.objects.all()

