from django.conf.urls import url

from notifs import views


# urls that performs operations
urlpatterns = [
    url(r'unread/$', views.unread, name='unread'),
    url(r'mark_as_read/(?P<pk>\d+)/$', views.mark_as_read, name='mark_as_read')
]
