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
        read_only_fields = ('pk', 'created_at')
        search_fields = (
            'person__user',
            'person__personal_email',
            'person__work_email'
        )


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = (
            'pk',
            'email'
        )
        read_only_fields = ('pk',)

    def validate_email(self, value):
        qs = Email.objects.filter(email__iexact=value)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError('Title must be unique')
        return value


class CoordinatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinates
        fields = (
            'pk',
            'latitude',
            'longitude'
        )
        read_only_fields = ('pk',)


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
        read_only_fields = ('pk',)


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
        read_only_fields = ('pk', 'created', )


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
        read_only_fields = ('pk', 'created', )


# serializers convert to JSON but also validate for data passed
