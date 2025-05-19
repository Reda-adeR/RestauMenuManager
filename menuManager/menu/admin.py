from django.contrib import admin

from .models import UserModel, MenuItem
# Register your models here.
admin.site.register(MenuItem)
admin.site.register(UserModel)
