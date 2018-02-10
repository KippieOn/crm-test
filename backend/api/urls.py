from django.conf.urls import url, include
from rest_framework.authtoken import views as drf_views
# from rest_framework import routers
from api.views import (ListViewSet, ListRUDView,
                       EmailViewSet, EmailRUDView,
                       CoordinatesViewSet, CoordinatesRUDView,
                       AddressViewSet, AddressRUDView,
                       ExtendedUserViewSet, ExtendedUserRUDView)

urlpatterns = [
    url(r'^list/(?P<pk>\d+)/$', ListRUDView.as_view(), name='see-lists'),
    url(r'^create/list/$', ListViewSet.as_view(), name='create-list'),
    url(r'^email/(?P<pk>\d+)/$', EmailRUDView.as_view(), name='see-emails'),
    url(r'^create/email/$', EmailViewSet.as_view(), name='create-email'),
    url(r'^coordinates/(?P<pk>\d+)/$', CoordinatesRUDView.as_view(),
        name='see-coordinates'),
    url(r'^create/coordinates/$', CoordinatesViewSet.as_view(),
        name='create-coordinates'),
    url(r'^address/(?P<pk>\d+)/$', AddressRUDView.as_view(),
        name='see-addresses'),
    url(r'^create/address/$', AddressViewSet.as_view(), name='create-address'),
    url(r'^user/(?P<pk>\d+)/$', ListRUDView.as_view(), name='see-users'),
    url(r'^create/user/$', ListViewSet.as_view(), name='create-user'),
    url(r'^list/user/$', ListViewSet.as_view(), name='create-user'),
    url(r'^auth$', drf_views.obtain_auth_token, name="auth"),
]
