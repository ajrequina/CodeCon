from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_api import views
from rest_api.views import AccountView
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'accounts', AccountView)


urlpatterns = [
    url(r'^', include(router.urls)),
]

urlpatterns = format_suffix_patterns(urlpatterns)