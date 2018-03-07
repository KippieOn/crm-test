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
    # email should be used for contact points
    email = models.CharField(_('Email'),
                             max_length=60,
                             blank=True,
                             null=True)

    def __str__(self):
        return "<Email: {}>".format(self.email)

    def get_email(self):
        return self.email


@python_2_unicode_compatible
class Coordinates(models.Model):
    # not a very relevant model - may be used to create visualizations
    # or for extra data processing
    latitude = models.CharField(_('latitude'),
                                max_length=10,
                                blank=True,
                                null=True)
    longitude = models.CharField(_('longitude'),
                                 max_length=10,
                                 blank=True,
                                 null=True)

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
    # do computations here


@python_2_unicode_compatible
class Address(models.Model):
    line1 = models.CharField(_('first line of the address'),
                             max_length=255,
                             blank=True,
                             null=True)
    line2 = models.CharField(_('second line of the address'),
                             max_length=255,
                             blank=True,
                             null=True)
    line3 = models.CharField(_('city'),
                             max_length=255,
                             blank=True,
                             null=True)
    state = models.CharField(_('state'),
                             max_length=100,
                             blank=True,
                             null=True)
    postcode = models.CharField(_('postcode'),
                                max_length=100,
                                blank=True,
                                null=True)
    coordinates = models.ForeignKey(Coordinates,
                                    on_delete=models.CASCADE,
                                    blank=True,
                                    null=True,
                                    related_name="coordinates")

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
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name="Person_details",
                             null=True)
    work_address = models.ForeignKey(Address,
                                     on_delete=models.CASCADE,
                                     blank=True,
                                     null=True,
                                     related_name="Work_address")
    home_address = models.ForeignKey(Address,
                                     on_delete=models.CASCADE,
                                     blank=True, null=True,
                                     related_name="Home_Address")
    work_email = models.ForeignKey(Email,
                                   on_delete=models.CASCADE,
                                   blank=True,
                                   null=True,
                                   related_name="work_email")
    personal_email = models.ForeignKey(Email,
                                       on_delete=models.CASCADE,
                                       blank=True,
                                       null=True,
                                       related_name="personal_email")
    phone_number = models.CharField(_('phone number'),
                                    max_length=18,
                                    blank=True)
    created = models.DateField(_('when the user was created'),
                               auto_now=False,
                               auto_now_add=True)
    last_modified = models.DateField(_('last time it was modified'),
                                     auto_now=True,
                                     auto_now_add=False)

    def __str__(self):
        return "{} model".format(self.user.first_name)

    class Meta:
        ordering = ('last_modified',)

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


@python_2_unicode_compatible
class EmailMessage(models.Model):
    from_whom = models.ForeignKey(Email,
                                  on_delete=models.CASCADE,
                                  blank=False,
                                  null=False,
                                  related_name="from_whom")
    to_whom = models.ForeignKey(Email,
                                on_delete=models.CASCADE,
                                blank=False,
                                null=False,
                                related_name="to_whom")
    subject = models.CharField(_('subject of the email'),
                               max_length=255,
                               blank=True,
                               null=True)
    body = models.CharField(_('body of the email'),
                            max_length=10000,
                            blank=True,
                            null=True)
    created = models.DateField(_('when it was created'),
                               auto_now=False,
                               auto_now_add=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return '<Email to {}>'.format(self.to_whom)

    def get_to(self):
        return self.to_whom

    def get_from(self):
        return self.from_whom

    def get_subject(self):
        return self.subject

    def get_body(self):
        return self.body

    def get_created_at(self):
        return self.created


@python_2_unicode_compatible
class List(models.Model):
    person = models.ForeignKey(ExtendedUser,
                               on_delete=models.CASCADE,
                               blank=True,
                               null=True,
                               related_name="person")
    name = models.CharField(_("List name/purpose"), max_length=120)
    description = models.CharField(_("Purpose of the list"),
                                   max_length=500,
                                   null=True,
                                   blank=True)
    updated_at = models.DateField(auto_now=True, auto_now_add=False)
    created_at = models.DateField(auto_now=False, auto_now_add=True)

    class Meta:
        ordering = ('updated_at', )

    def __str__(self):
        if self.person is None:
            return '<An empty list with name {} , created at: {}, updated at: {}'\
                    .format(self.name,
                            self.created_at,
                            self.updated_at)
        else:
            return '<List with name {}, {} contacts, created at: {}, updated at: {}'\
                    .format(self.name,
                            len(self.person),
                            self.created_at,
                            self.updated_at)

    def get_person(self):
        return self.person

    def get_name(self):
        return self.name

    def get_updated_at(self):
        return "Last updated on :{dfmt} {tfmt}"\
                .format(self.updated_at, dfmt='%d/%m/%Y', tfmt='%H:%M')

    def get_created_at(self):
        return "Created on {}/{}/{} at {}:{}"\
                .format(self.created_at.day,
                        self.created_at.month,
                        self.created_at.year,
                        self.created_at.hour,
                        self.created_at.minute)
