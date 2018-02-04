from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


def is_password_hash(string):
    """
    Check if provided string is a password hash. Could do something fancier
    with a regex here instead of navie length check.
    """
    return len(string) == settings.PASSWORD_HASH_LENGTH


class User(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subscribed = models.BooleanField(default=True, null=False)

    def save(self, *args, **kwargs):
        """
        Reset the users password if a new password is provided. This is used
        in Django Admin
        """
        if self.pk and is_password_hash(self.password) is False:
            self.set_password(self.password)
        super().save(*args, **kwargs)


class SavedCard(models.Model):
    """
    Model represents a saved credit card stored in Stripe.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    card_token = models.CharField(max_length=100,
                                  blank=False,
                                  null=False)
    last4 = models.CharField(max_length=4,
                             blank=False,
                             null=False)
    brand = models.CharField(max_length=20,
                             blank=False,
                             null=False)

    def __str__(self):
        return '{} ending {} for {}'.format(self.brand,
                                            self.last4,
                                            self.user)
