from django.contrib import admin
from inventory.models import Style, Supplier, Item, Rawmaterial

# Register your models here.
admin.site.register(Style)
admin.site.register(Supplier)
admin.site.register(Item)
admin.site.register(Rawmaterial)
