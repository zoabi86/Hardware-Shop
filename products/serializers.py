from rest_framework import serializers
from .models import Product, Category, default_sizes
import json
        
class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = ['url', 'id', 'name', 'barcode', 'category', 'category_name', 'sizes', 'stock_count', 'price', 'product_description', 'image']

    def create(self, validated_data):
        if 'sizes' not in validated_data or validated_data['sizes'] is None:
            validated_data['sizes'] = default_sizes()
        return super().create(validated_data)

    def get_category_name(self, obj):
        return obj.category.name if obj.category else None

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
