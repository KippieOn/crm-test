from django.conf.urls import url, include
from rest_framework.authtoken import views as drf_views
from rest_framework import routers
from api.views import ListViewSet

urlpatterns = [
    #url(r'^', include(router.urls)),
    url(r'^(?P<name>\w+)/$', ListViewSet.as_view(), name='Lists'),
    url(r'^auth$', drf_views.obtain_auth_token, name="auth"),
]
