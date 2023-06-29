from django.contrib import admin
from .models import Product, ProductCategory


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'category', )


# admin.site.register(Product)
# admin.site.register(ProductCategory)
