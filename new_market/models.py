from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField(default=0.0)


class Staff(models.Model):
    full_name = models.CharField(max_length=255)
    position_ = models.CharField(max_length=255)
    labor_contract = models.IntegerField(default=0)
