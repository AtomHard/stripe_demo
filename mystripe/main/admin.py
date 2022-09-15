from django.contrib import admin
from .models import *


class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price',)
    list_display_links = ('id', 'name', )
    search_fields = ('name', )

    save_on_top = True


admin.site.register(Item, ItemAdmin)
