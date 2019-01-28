from django.contrib import admin # Register your models here.
from .models import Product, Maschine, Componentmaschine

admin.site.register(Product)
admin.site.register(Maschine)
admin.site.register(Componentmaschine)