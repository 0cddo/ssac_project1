from django.db import models

# Create your models here.

class Consumption(models.Model):
    buy_date = models.CharField(max_length=20, null=True)
    gender = models.CharField(max_length=10, null=True)
    age = models.CharField(max_length=10, null=True)
    product = models.CharField(max_length=50, null=True)
    total = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.buy_date