from django.conf.urls import url

from profiles import views


urlpatterns = [
    url(r'^settings/$', views.settings_page, name='setting'),
    url(r'^change-info/$', views.change_info, name='change_info'),
    url(r'^change-credentials/$', views.change_credentials, name='change_credentials'),
    url(r'^change-password/$', views.change_password, name='change_password'),
    url(r'^change-profpic/$', views.change_profile_photo, name='change_profpic'),
    url(r'^change-coverpic/$', views.change_cover_photo, name='change_coverpic'),
    url(r'^follow/(?P<pk>\d+)/$', views.follow, name='follow'),
    url(r'^unfollow/(?P<pk>\d+)/$', views.unfollow, name='unfollow'),
     url(r'^follow_page/(?P<pk>\d+)/(?P<page_type>[a-zA-Z]+)/$', views.follow_page, name='follow_page'),
]
