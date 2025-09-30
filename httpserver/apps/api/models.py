from django.db import models
from uuid import uuid4

DEFAULT_DATE = '2025-01-01 00:00:00'

class Card(models.Model):
    id = models.CharField(default=uuid4, primary_key=True)
    number = models.CharField(max_length=4, default='')

class Category(models.Model):
    id = models.CharField(default=uuid4, primary_key=True)
    name = models.CharField(max_length=150, default='')
    description = models.CharField(max_length=150, default='')

class Registry(models.Model):
    id = models.CharField(default=uuid4, primary_key=True)
    title = models.CharField(max_length=150, default='')
    value = models.DecimalField(default=0, max_digits=9, decimal_places=2)
    datetime = models.DateTimeField(default=DEFAULT_DATE)
    description = models.CharField(max_length=150, default='')
    card = models.ForeignKey(Card, default=None, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, default=None, on_delete=models.CASCADE)