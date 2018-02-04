import logging

from django.conf import settings
import stripe
import paypalrestsdk

from user.models import SavedCard


log = logging.getLogger(__name__)


def get_friendly_decline_message():
    return 'The transaction was declined by your bank - ' \
           'please check your card details and try again.'


def get_friendly_error_message():
    return 'An error occurred when communicating with ' \
           'the payment gateway.'


class PayPalAPI:
    def __init__(self, basket):
        sandbox = settings.PAYPAL_SANDBOX_MODE

        if not sandbox:
            credentials = settings.PAYPAL_CREDENTIALS['live']
        else:
            credentials = settings.PAYPAL_CREDENTIALS['sandbox']

        if basket.currency == 'USD':
            credentials = credentials['US']
        else:
            credentials = credentials['UK']

        self.api = paypalrestsdk.Api({
            'mode': 'sandbox' if sandbox else 'live',
            'client_secret': credentials['client_secret'],
            'client_id': credentials['client_id'],
        })

    def payment(self, data):
        return paypalrestsdk.Payment(data, api=self.api)

    def execute(self, payment, buyer):
        payment = paypalrestsdk.Payment.find(payment, api=self.api)
        if not payment.execute({'payer_id': buyer}):
            log.error(payment.__dict__)
            msg = get_friendly_error_message()
            #raise InvalidGatewayRequestError(msg)


class Facade(object):
    def __init__(self):
        stripe.api_key = settings.STRIPE_SECRET_KEY

    def create_card(self, user, stripe_token):
        card = stripe.Customer.create(source=stripe_token)
        last4 = card.sources.data[0]['last4']
        brand = card.sources.data[0]['brand']
        defaults = {
            'card_token': card.id,
        }
        card, _ = SavedCard.objects.update_or_create(user=user,
                                                     last4=last4,
                                                     brand=brand,
                                                     defaults=defaults)
        return card

    def charge_card(self,
                    order_number,
                    total,
                    card_token,
                    currency=settings.STRIPE_CURRENCY):
        try:
            charge = stripe.Charge.create(
                amount=int(total.incl_tax * 100),
                currency=currency,
                customer=card_token,
                metadata={'order_number': order_number},
            )
            return charge.id

        except stripe.CardError:
            msg = get_friendly_decline_message()
#            raise UnableToTakePayment(msg)
        except stripe.StripeError:
            msg = get_friendly_error_message()
            # raise InvalidGatewayRequestError(msg)
