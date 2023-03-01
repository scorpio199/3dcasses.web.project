from django.contrib import admin

from .models import Marketplace, Transaction

admin.site.register(Marketplace)
admin.site.register(Transaction)