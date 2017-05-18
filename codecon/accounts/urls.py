from django.conf.urls import url

from accounts import views

urlpatterns = [
    url(r'^login/$', views.login_user, name='login'),
    url(r'^logout/$', views.logout_user, name='logout'),
    url(r'^register/$', views.register_user, name='register'),
    url(r'^$',  views.account_form, name='account_form'),
]
