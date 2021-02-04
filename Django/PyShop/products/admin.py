from django.contrib import admin
from .models import Product, Offer


class OfferAdmin(admin.ModelAdmin):
    #Tuple
    list_display = ('code', 'discount')


class ProductAdmin(admin.ModelAdmin):
    #Tuple
    list_display = ('name', 'price','stock')

admin.site.register(Offer, OfferAdmin)
admin.site.register(Product, ProductAdmin)



