SATCHLESS_DEFAULT_CURRENCY = 'EUR'

SATCHLESS_IMAGE_SIZES = {
    'product-detail': {
        'size': (200, 150),
        'crop': False,
    }
}

SATCHLESS_PRICING_HANDLERS = [
    'satchless.contrib.pricing.simpleqty.SimpleQtyPricingHandler',
]
SATCHLESS_ORDER_PARTITIONERS = [
    'satchless.contrib.order.partitioner.simple',
]
SATCHLESS_DELIVERY_PROVIDERS = [
    'satchless.contrib.delivery.simplepost.PostDeliveryProvider',
]

SATCHLESS_PAYMENT_PROVIDERS = [
    'satchless.contrib.payment.django_payments_provider.DjangoPaymentsProvider',
    'satchless.contrib.payment.mamona_provider.MamonaProvider',
]

# This setting specifies which payment channels of django-payments
# will be available to Satchless.
SATCHLESS_DJANGO_PAYMENT_TYPES = ('dummy',)