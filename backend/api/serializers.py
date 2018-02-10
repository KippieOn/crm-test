from rest_framework import serializers
from crm.models import (List, ExtendedUser, Email,
                        Coordinates, Address, EmailMessage)


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = (
            'pk',
            'name',
            'person',
            'updated_at',
            'created_at',
        )


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = (
            'pk',
            'email'
        )


class CoordinatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinates
        fields = (
            'pk',
            'latitude',
            'longitude'
        )


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = (
            'pk',
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
            'pk',
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
            'pk',
            'user',
            'work_address',
            'home_address',
            'work_email',
            'personal_email',
            'phone_number',
            'created',
            'last_modified',
        )


# serializers convert to JSON but also validate for data passed
