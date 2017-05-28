from django.conf.urls import url

from search import views


urlpatterns = [
    url(r'^$', views.search_page, name='results'),
    url(r'^results/$', views.search_results, name='search_results'),
]
