from django.db import models
from django.core.urlresolvers import reverse

class Consumption(models.Model):
    consumer = models.CharField(max_length=120)
    total = models.FloatField()

    def get_absolute_url(self):
        return reverse('badala:detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.consumer

class Product(models.Model):
    consumption = models.ForeignKey(Consumption, on_delete=models.CASCADE)
    description = models.CharField(max_length=250)
    price = models.FloatField()

    def __str__(self):
        return self.description