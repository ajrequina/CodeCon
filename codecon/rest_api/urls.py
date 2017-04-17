from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from rest_api import views


urlpatterns = [
	url(r'^posts$', views.PostList.as_view()),
	url(r'^posts/(?P<pk>[0-9]+)$', views.PostDetail.as_view()),
	url(r'^users$', views.UserList.as_view()),
	url(r'^users/(?P<pk>[0-9]+)$', views.UserDetail.as_view()),
	url(r'^users/register', views.register_user),
	url(r'^users/login', views.login_user),
]

urlpatterns = format_suffix_patterns(urlpatterns)
