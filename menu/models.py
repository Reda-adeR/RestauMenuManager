from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class MenuItem(models.Model):
    itemName = models.CharField(max_length=100)
    itemPrice = models.IntegerField(default=0)

class CustomUser(AbstractUser):
    pass