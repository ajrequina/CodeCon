from django.conf.urls import url

from posts import views


# urls that performs operations
urlpatterns = [
    url(r'add/$', views.add, name='add'),
    url(r'update/(?P<pk>\d+)/$', views.update, name='update'),
    url(r'delete/(?P<pk>\d+)/$', views.delete, name='delete'),
    url(r'detail/(?P<pk>\d+)/$', views.detail, name='detail'),
    url(r'like/(?P<post_id>\d+)/$', views.like, name='like'),
    url(r'(?P<page_type>[a-zA-Z]+)/(?P<user_id>\d+)$', views.list, name='list'),
    url(r'(?P<page_type>[a-zA-Z]+)/$', views.list, name='list'),
    url(r'top10/$', views.top10, name='top10'),
    url(r'$', views.list, name='list'),
]
