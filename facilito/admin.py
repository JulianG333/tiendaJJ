from django.contrib import admin

from .models import Product

class ProductAdmin(admin.ModelAdmin):
    fields = ('title', 'description', 'print', 'image')
    list_display = ('__str__', 'slug')
admin.site.register(Product, ProductAdmin)
