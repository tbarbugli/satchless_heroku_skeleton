from django.conf.urls.defaults import patterns, include, url
from satchless.category.app import product_app
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^products/', include(product_app.urls)),
    url(r'^contact/', include('satchless.contact.urls')),
    url(r'^image/', include('satchless.image.urls')),
    url(r'^cart/', include('satchless.cart.urls')),
    url(r'^checkout/', include('satchless.order.urls')),
)
