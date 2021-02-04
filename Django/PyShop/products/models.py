from django.db import models


class Product(models.Model):
    #CharField allows to contain textual data
    name = models.CharField(max_length=255)
    #FloatField allow to contain floating decimal numbers
    price = models.FloatField()
    #IntegerField allows to contain integer numbers
    stock = models.IntegerField()
    #Standard max length of URLs
    image_url = models.CharField(max_length=2083)

class Offer(models.Model):
    #CharField allows to contain textual data
    code =  models.CharField(max_length=10)
    #CharField allows to contain textual data
    description = models.CharField(max_length=255)
    #FloatField allow to contain floating decimal numbers
    discount = models.FloatField()
