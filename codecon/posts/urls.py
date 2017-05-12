from django.conf.urls import url

from posts import views

urlpatterns = [
    url(r'^$', views.home_page, name='homepage'),
    url(r'^add$', views.add_post, name='add_post'),
    url(r'^update/(?P<pk>\d+)/$', views.update_post, name='update_post'),
    url(r'^delete/(?P<pk>\d+)/$', views.delete_post, name='delete_post'),
    url(r'^addpage$', views.add_post_page, name='add_post_page'),
    url(r'^updatepage/(?P<pk>\d+)/$', views.update_post_page, name='update_post_page'),
    url(r'^detail/(?P<pk>\d+)/$', views.post_detail, name="post_detail"),
    url(r'^like/(?P<pk>\d+)/$', views.like_post, name="like_post"),
    url(r'^all$', views.view_posts, name='view_posts')
]
