from django.conf.urls import url

from profiles import views


urlpatterns = [
    url(r'^settings/$', views.settings_page, name='setting'),
    url(r'^change-info/$', views.change_info, name='change_info'),
    url(r'^change-credentials/$', views.change_credentials, name='change_credentials'),
    url(r'^change-password/$', views.change_password, name='change_password'),
]
