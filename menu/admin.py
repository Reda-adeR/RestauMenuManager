from django.contrib import admin

# Register your models here.
from .models import MenuItem, CustomUser
admin.site.register(MenuItem)
admin.site.register(CustomUser)