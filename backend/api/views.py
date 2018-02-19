# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import get_object_or_404

from rest_framework import generics, mixins
from rest_framework.authentication import (SessionAuthentication,
                                           BasicAuthentication)

from rest_framework.decorators import (api_view, authentication_classes,
                                       permission_classes)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from crm.models import (List, ExtendedUser, Email,
                        Coordinates, Address, EmailMessage)
from api.serializers import (ListSerializer, ExtendedUserSerializer,
                             EmailSerializer, CoordinatesSerializer,
                             AddressSerializer, EmailMessageSerializer)


# Basic token authentication
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


class ListViewSet(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = ListSerializer

    def get_queryset(self):
        qs = List.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(
                    Q(name__icontains=query) |
                    Q(ExtendedUser__personal_email__icontains=query) |
                    Q(ExtendedUser__work_email__icontains=query)
                    ).distinct()
        return qs

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ListRUDView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = ListSerializer

    def get_queryset(self):
        qs = List.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(
                Q(name__icontains=query)
                ).distinct()
        return qs


class EmailViewSet(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = EmailSerializer

    def get_queryset(self):
        qs = Email.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(email__icontains=query).distinct()
        return qs

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class EmailRUDView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = EmailSerializer

    def get_queryset(self):
        qs = Email.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(email__icontains=query).distinct()
        return qs


class CoordinatesViewSet(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = CoordinatesSerializer

    def get_queryset(self):
        qs = Coordinates.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(
                    Q(latitude__icontains=query) |
                    Q(longitude__icontains=query)
                    )
        return qs

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CoordinatesRUDView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = CoordinatesSerializer

    def get_queryset(self):
        qs = Coordinates.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(
                Q(line1__icontains=query) |
                Q(line3__icontain=query) |
                Q(postcode_icontains=query)
                )
        return qs


class AddressViewSet(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = AddressSerializer

    def get_queryset(self):
        qs = Address.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(
                    Q(line1__icontains=query) |
                    Q(line3__icontain=query) |
                    Q(postcode_icontains=query)
                    )
        return qs

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class AddressRUDView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = AddressSerializer

    def get_queryset(self):
        qs = Address.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(
                Q(name__icontains=query)
                ).distinct()
        return qs


class ExtendedUserViewSet(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = ExtendedUserSerializer

    def get_queryset(self):
        qs = ExtendedUser.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(
                    Q(personal_email__icontains=query) |
                    Q(address__icontains=query) |
                    Q(work_email__icontains=query) |
                    Q(phone_number__icontains=query)
                    ).distinct()
        return qs

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ExtendedUserRUDView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = ExtendedUserSerializer

    def get_queryset(self):
        qs = ExtendedUser.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(
                Q(personal_email__icontains=query) |
                Q(address__icontains=query) |
                Q(work_email__icontains=query) |
                Q(phone_number__icontains=query)
                ).distinct()
        return qs
