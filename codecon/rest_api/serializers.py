from rest_framework import serializers
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

from rest_api.models import Post

class UserSerializer(serializers.ModelSerializer):
	posts = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all(), required=False)
	password = serializers.CharField(write_only=True)
	first_name = serializers.CharField(required=True)
	last_name = serializers.CharField(required=True)
	email = serializers.EmailField(required=True)
	confirm_password = serializers.CharField(write_only=True)

	def create(self, validated_data):
		user = User.objects.create(
				username=validated_data['username'],
				first_name=validated_data['first_name'],
				last_name=validated_data['last_name'],
				email=validated_data['email'],
			)
		user.set_password(validated_data['password'])
		user.save()
		return user

	def to_internal_value(self, data):
		errors = []
		if "email" not in data or data["email"] == None or data["email"] == "":
			errors.append("Email address is required.")
		else:
			try:
				validate_email(data["email"])
				if User.objects.filter(email=data["email"]).count() > 0:
					errors.append("Email address already exists.")
			except ValidationError as e:
				errors.append("Email address is invalid.")
		if "username" not in data or data["username"] == "" or data["username"] == None:
			errors.append("Username is required.")
		else:
			if User.objects.filter(username=data["username"]).count() > 0:
				errors.append("Username already exists.")
		if "first_name" not in data or data["first_name"] == "" or data["first_name"] == None:
			errors.append("Firstname is required.")
		if "last_name" not in data or data["last_name"] == "" or data["last_name"] == None:
			errors.append("Lastname is required.")
		if "password" not in data or data["password"] == "" or data["password"] == None:
			errors.append("Password is required.")
		else:
			if len(data['password']) < 8:
				errors.append("Password must be at least 8 characters.")
			elif data['password'] != data['confirm_password']:
				errors.append("Passwords do not match.")
		if len(errors) > 0:
			raise serializers.ValidationError({"status" : False, "details" : errors})
		return super(UserSerializer, self).to_internal_value(data)
	class Meta:
		model = User
		fields = ('id', 'first_name', 'last_name', 
			      'username', 'password', 'confirm_password',
			      'email', 'posts')

class PostSerializer(serializers.ModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')

	class Meta:
		model = Post
		fields = ('id', 'title', 'content', 'owner', )