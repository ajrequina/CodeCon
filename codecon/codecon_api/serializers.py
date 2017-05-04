from rest_framework import serializers
from django.contrib.auth.models import User

class RegisterSerializer(serializers.ModelSerializer):
	first_name = serializers.CharField(required=True)
	last_name = serializers.CharField(required=True)
	username = serializers.CharField(required=True)
	email = serializers.CharField(required=True)
	password = serializers.CharField(required=True)

	def create(self, data):
		user = User.objects.create(
				first_name=data["first_name"],
				last_name=data["last_name"],
				username=data["username"],
				email=data["email"],
			)
		user.set_password(data["password"])
		user.save()
		return user
	
	class Meta:
		model = User
		fields = ('id', 'first_name', 'last_name', 
			      'username', 'email',
			      'password',)

