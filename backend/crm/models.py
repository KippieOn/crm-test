from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

# TODO:
#     - contact model
#     - use properties
#     - use better fields


@python_2_unicode_compatible
class Email(models.Model):
    # email should be used for contaact points
    email = models.CharField(_('Email'), max_length=60,
                             blank=True)

    def __str__(self):
        return "Email for {}".format(self.user)

    def get_email(self):
        return self.email


@python_2_unicode_compatible
class Coordinates(models.Model):
    # not a very relevant model - may be used to create visualizations
    # or for extra data processing
    latitude = models.CharField(_('latitude'), max_length=10, blank=True)
    longitude = models.CharField(_('longitude'), max_length=10, blank=True)

    def __str__(self):
        return "<{} lat, {} long>".format(self.latitude, self.longitude)

    def latitude(self):
        return self.latitude

    def longitude(self):
        return self.longitude

    def lat_float(self):
        return float(self.latitude)

    def long_float(self):
        return float(self.longitude)


@python_2_unicode_compatible
class Address(models.Model):
    line1 = models.CharField(_('first line of the address'),
                             max_length=255, blank=True)
    line2 = models.CharField(_('second line of the address'),
                             max_length=255, blank=True)
    line3 = models.CharField(_('third line of the address'),
                             max_length=255, blank=True)
    state = models.CharField(_('state'), max_length=100, blank=True)
    postcode = models.CharField(_('postcode'), max_length=100, blank=True)

    def __str__(self):
        return "<Address model for postcode: {}>".format(self.postcode)

    def get_line1(self):
        return self.line1

    def get_line2(self):
        return self.line2

    def get_line3(self):
        return self.line3

    def get_state(self):
        return self.state

    def get_postcode(self):
        return self.postcode


@python_2_unicode_compatible
class ExtendedUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    work_address = models.ForeignKey(Address, on_delete=models.CASCADE,
                                     blank=True)
    home_address = models.ForeignKey(Address, on_delete=models.CASCADE,
                                     blank=True)
    phone_number = models.CharField(_('phone number'), max_length=18,
                                    blank=True)
    created = models.DateField(_('when the user was created'),
                               auto_now=False, auto_now_add=True)
    last_modified = models.DateField(_('last time it was modified'),
                                     auto_now=True, auto_now_add=False)

    def __str__(self):
        return "{} model".format(self.user.name)

    class Meta:
        order_by = ['last_contacted']

    def get_user(self):
        return self.user

    def get_work_address(self):
        return self.work_address

    def get_home_address(self):
        return self.home_address

    def get_phone_number(self):
        return self.phone_number

    def get_created(self):
        return self.created

    def get_last_modified(self):
        return self.last_modified
