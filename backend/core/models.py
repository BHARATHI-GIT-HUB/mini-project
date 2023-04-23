from django.db import models


# Create your models here.
class Product(models.Model):
    productId = models.AutoField(primary_key=True)
    url = models.TextField()
    name = models.CharField(max_length=100, null=True, blank=True)
    oneLine = models.TextField(null=True, blank=True)


class Review(models.Model):
    commands = models.TextField()
    productId = models.ForeignKey(Product, on_delete=models.CASCADE)
