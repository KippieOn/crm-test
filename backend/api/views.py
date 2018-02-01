# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.authentication import (SessionAuthentication,
                                           BasicAuthentication)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


@api_view(['GET'])
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated))
def login_view(request, format_none):
    user = User.objects.get(email=request.user)
    print(user)
    content = {
        'user': unicode(user.username),
        'auth': unicode(request.auth),
    }
    return Response(content)
