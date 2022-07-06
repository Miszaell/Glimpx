from django.contrib import admin
from apps.products.models import Material, Medicine, Stock

admin.site.register(Material)
admin.site.register(Medicine)
admin.site.register(Stock)
