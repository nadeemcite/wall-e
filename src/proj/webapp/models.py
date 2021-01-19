from django.db import models
from django.contrib.postgres import fields as pg

# Create your models here.
class Product(models.Model):
    product_id = models.IntegerField(null=True)
    name = models.CharField(max_length=5000, null=True)
    mrp = models.CharField(max_length=10,null=True)
    discountprice = models.CharField(max_length=10,null=True)

    def __str__(self):
        return self.name
