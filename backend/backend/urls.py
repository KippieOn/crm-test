from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from rest_framework import include_docs_urls
from api import views as crm_api

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^api/', include('api.urls')),
    url(r'^docs/', include_docs_urls(title="crm api")),
]
