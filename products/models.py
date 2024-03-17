from django.db import models
import json  # Import the json module

def default_sizes():
    return {"1/2": None, "3/4": None, "1 1/4": None, "1 1/2": None}

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def is_root(self):
        return self.parent is None

    def get_children(self):
        return Category.objects.filter(parent=self)

    def get_ancestors(self):
        ancestors = []
        parent = self.parent
        while parent is not None:
            ancestors.append(parent)
            parent = parent.parent
        return ancestors

class Product(models.Model):
    name = models.CharField(max_length=100)
    barcode = models.CharField(max_length=100, unique=True, default='12345678')
    # ForeignKey to link each product to a specific category
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    sizes = models.JSONField(default=default_sizes, null=True, blank=True) 
    stock_count = models.IntegerField(default='100')
    price = models.DecimalField(max_digits=6, decimal_places=2, default='19.99')
    product_description = models.TextField(default='This is a generic product')
    image = models.ImageField(upload_to='product_images/', default='product_images/default.jpg')

    def __str__(self):
        return self.name
