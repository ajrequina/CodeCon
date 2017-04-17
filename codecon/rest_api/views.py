from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from rest_framework.decorators import api_view, permission_classes
from django.http import Http404
from django.contrib.auth.models import User

from rest_api.models import Post
from rest_api.serializers import PostSerializer, UserSerializer
from rest_api.permissions import IsOwnerOrReadOnly

@api_view(['POST'])
@permission_classes([permissions.AllowAny,])
def register_user(request, format=None):
	if request.method == "POST":
		serializer = UserSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			result = {"status" : True, "details" : "User Successfully Registered."}
			return Response(result)
		return Response(serializer.errors)

@api_view(['POST'])
@permission_classes([permissions.AllowAny,])
def login_user(request, format=None):
	if request.method == "POST":
		pass
	return Response({"detail" : "Successfully Logged In"})

class UserList(APIView):
	def get(self, request, format=None):
		users = User.objects.all()
		serializer = UserSerializer(users, many=True)
		return Response(serializer.data)

class UserDetail(APIView):

	def get_object(self, pk):
		try:
			return User.objects.get(pk=pk)
		except User.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		user = self.get_object(pk)
		serializer = UserSerializer(user)
		return Response(serializer.data)

class PostList(APIView):
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, 
						  IsOwnerOrReadOnly, )

	def get(self, request, format=None):
		posts = Post.objects.all()
		serializer = PostSerializer(posts, many=True)
		return Response(serializer.data)
	
	def post(self, request, format=None):
		serializer = PostSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save(owner=self.request.user)
			return Response(serializer.data)
		return Response(serializer.errors)

class PostDetail(APIView):
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, 
						  IsOwnerOrReadOnly, )

	def get_object(self, pk):
		try:
			return Post.objects.get(pk=pk)
		except Post.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		post = self.get_object(pk)
		serializer = PostSerializer(post)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		post = self.get_object(pk)
		serializer = PostSerializer(post, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors)

	def delete(self, request, pk, format=None):
		post = self.get_object(pk)
		post.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
		