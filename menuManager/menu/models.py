from django.db import models

# Create your models here.
class MenuItem(models.Model):
    itemName  = models.CharField(max_length=30)
    itemPrice = models.IntegerField(default=0)

class UserModel(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password     = models.CharField(max_length=100)
    # email    = models.EmailField( unique=True )