from django.conf.urls import url

from comments import views


# urls that performs operations
urlpatterns = [
    url(r'add/(?P<post_id>\d+)/$', views.add, name='add'),
    url(r'update/(?P<pk>\d+)/$', views.update, name='update'),
    url(r'delete/(?P<pk>\d+)/$', views.delete, name='delete'),
]
