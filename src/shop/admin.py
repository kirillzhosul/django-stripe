"""
    Admin panel configuration as it is used.
"""

from django.contrib import admin
from shop.models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass
