from mamona.utils import get_backend_choices

from satchless.payment import PaymentProvider, ConfirmationFormNeeded
from . import models
from . import listeners

class MamonaProvider(PaymentProvider):
    unique_id = 'mamona'

    def enum_types(self, order=None, customer=None):
        return get_backend_choices()

    def create_variant(self, order, typ, form):
        variant = models.MamonaPaymentVariant.objects.get_or_create(order=order,
                                                                    price=0)[0]
        models.Payment.objects.create(order=variant, amount=order.total().gross,
                                      currency=order.currency, backend=typ)
        return variant

    def confirm(self, order):
        payment = order.paymentvariant.get_subtype_instance().payments.get()
        form = payment.get_processor().get_confirmation_form(payment)
        raise ConfirmationFormNeeded(**form)

provider = MamonaProvider()

listeners.start_listening()
