from django.conf.urls import url

from posts import views

urlpatterns = [
    url(r'^$', views.home_page, name='homepage'),
    url(r'^add_new$', views.add_post, name='add_post'),
    url(r'^add_post_page$', views.add_post_page, name='add_post_page'),


    url(r'^all$', views.view_posts, name='view_posts')
]
