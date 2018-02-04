from rest_framework import serializers
from crm.models import (List, ExtendedUser, Email,
                        Coordinates, Address, EmailMessage)


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = (
            'id',
            'name',
            'person',
            'updated_at',
            'created_at',
        )


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = (
            'id',
            'email'
        )


class CoordinatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinates
        fields = (
            'id',
            'latitude',
            'longitude'
        )


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = (
            'id',
            'line1',
            'line2',
            'line3',
            'state',
            'postcode',
            'coordinates'
        )



class EmailMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailMessage
        fields = (
            'id',
            'to_whom',
            'from_whom',
            'subject',
            'body',
            'created',
        )


class ExtendedUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExtendedUser
        fields = (
            'id',
            'user',
            'work_address',
            'home_address',
            'work_email',
            'personal_email',
            'phone_number',
            'created',
            'last_modified'
        )
