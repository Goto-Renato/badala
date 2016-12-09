from django.contrib.auth.models import User
from django.db import models

class Product(models.Model):
    consumption = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=250)
    price = models.FloatField()

    def __str__(self):
        return self.description