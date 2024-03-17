from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['category__name', 'name', 'barcode']  # Add fields you want to search by

    def get_queryset(self):
        queryset = Product.objects.all()  # Default queryset
        search_term = self.request.query_params.get('query', None)
        if search_term is not None:
            queryset = queryset.filter(category__name__icontains=search_term)
        return queryset

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


