from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from ..util import countries

class Address(models.Model):
    customer = models.ForeignKey('Customer', related_name='addressbook')
    alias = models.CharField(_("short alias"), max_length=30,
            help_text=_("User-defined alias which identifies this address"))
    full_name = models.CharField(_("full person name"), max_length=256)
    company_name = models.CharField(_("company name"), max_length=256, blank=True)
    street_address_1 = models.CharField(_("street address 1"), max_length=256)
    street_address_2 = models.CharField(_("street address 2"), max_length=256, blank=True)
    city = models.CharField(_("city"), max_length=256)
    postal_code = models.CharField(_("postal code"), max_length=20)
    country = models.CharField(_("country"), choices=countries.COUNTRY_CHOICES, max_length=2)
    country_area = models.CharField(_("country administrative area"), max_length=128)
    tax_id = models.CharField(_("tax ID"), max_length=40, blank=True)
    phone = models.CharField(_("phone number"), max_length=30, blank=True)

    def __unicode__(self):
        return self.alias


class CustomerManager(models.Manager):
    def get_or_create_for_user(self, user):
        try:
            return self.get(user=user)
        except Customer.DoesNotExist:
            return Customer.objects.create(user=user, email=user.email)


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True)
    billing_address = models.ForeignKey(Address, related_name='billing_customers', null=True, blank=True)
    shipping_address = models.ForeignKey(Address, related_name='shipping_customers', null=True, blank=True)
    email = models.EmailField(_("email"))

    objects = CustomerManager()

    def __unicode__(self):
        return self.email

    def save(self, *args, **kwargs):
        super(Customer, self).save(*args, **kwargs)
        if self.user:
            self.user.email = self.email
            self.user.save()
