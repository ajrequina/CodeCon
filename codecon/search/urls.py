from django.conf.urls import url

from search import views


urlpatterns = [
    url(r'^$', views.search_page, name='results'),
]
