# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.authentication import (SessionAuthentication,
                                           BasicAuthentication)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from crm.models import (List, ExtendedUser, Email,
                        Coordinates, Address, EmailMessage)

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



@api_view(['POST'])
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated))
def create_list(request, name):
    new_list = List.objects.create(
        name=name,
    )
    new_list.save()
    return new_list


@api_view(['GET'])
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated))
def retrieve_list(request, name):
    list_object = List.objects.get_object_or_404(List, name=name)
    return list_object


@api_view(['PATCH'])
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated))
def retrieve_lists(request):
    lists = List.objects.all()
    return lists


@api_view(['DELETE'])
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated))
def update_list(request, what_to_update):
    pass


@api_view(['POST'])
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated))
def delete_list(request, name):
    to_delete = List.objects.get(name=name)
    del to_delete
