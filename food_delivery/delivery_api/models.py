# delivery_api/models.py

from django.db import models

class Organization(models.Model):
    name = models.CharField(max_length=100)

class Item(models.Model):
    TYPE_CHOICES = (
        ('perishable', 'Perishable'),
        ('non_perishable', 'Non-Perishable'),
    )
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    description = models.CharField(max_length=255)

class Pricing(models.Model):
    organization_id = models.CharField(max_length=20)
    item_id = models.CharField(max_length=20)
    zone = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=1.5)

