from django.contrib import admin
from .models import Thing
# after making models we import them here

admin.site.register(Thing)
# Register your models here.
