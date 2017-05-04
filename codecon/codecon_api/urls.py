from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from codecon_api import views

router = DefaultRouter()
router.register(r'register', views.RegisterViewSet , 'Register')

urlpatterns = router.urls
