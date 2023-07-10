from django.contrib import admin
from .models import Product, ProductCategory


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'category', )
    prepopulated_fields = {'slug': ('name',)}


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
    prepopulated_fields = {'slug': ('name',)}


# admin.site.register(Product)
# admin.site.register(ProductCategory)
