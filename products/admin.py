from django.contrib import admin
from .models import Product
from .models import Category

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'barcode', 'category', 'stock_count', 'price']
    search_fields = ['name', 'category']

from django.contrib import admin

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Customize as needed

