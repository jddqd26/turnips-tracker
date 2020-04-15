from django.contrib import admin
from .models import Client, Island, Turnip_info

# Register your models here.
admin.site.register(Client)
admin.site.register(Island)
admin.site.register(Turnip_info)