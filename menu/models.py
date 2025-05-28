from django.db import models

# Create your models here.
class MenuItem(models.Model):
    itemName = models.CharField(max_length=100)
    itemPrice = models.IntegerField(default=0)