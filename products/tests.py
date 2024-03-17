from django.test import TestCase
from .models import Product, Category
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

class ProductModelTest(TestCase):
    def setUp(self):
        # Setup run before every test method.
        Category.objects.create(name="Electronics")
        Product.objects.create(
            name="Test Product",
            barcode="123456789012",
            category=Category.objects.get(name="Electronics"),
            stock_count=10,
            price=19.99
        )

    def test_product_creation(self):
        product = Product.objects.get(name="Test Product")
        self.assertEqual(product.name, "Test Product")

    def test_product_deletion(self):
        product = Product.objects.get(name="Test Product")
        product.delete()
        self.assertEqual(Product.objects.count(), 0)

class ProductViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        Category.objects.create(name="Electronics")
        self.product_data = {
            'name': 'New Product',
            'barcode': '123456789012',
            'category': Category.objects.get(name="Electronics").id,
            'stock_count': 20,
            'price': 29.99
        }
        self.response = self.client.post(
            reverse('product-list'),
            self.product_data,
            format="json")

    def test_api_can_create_a_product(self):
        print(self.response.data)
        # Check that the product was created with the correct category name
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.response.data['category_name'], 'Electronics')

    def test_api_can_get_a_product_list(self):
        response = self.client.get(
            reverse('product-list'),
            format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

    def test_api_can_delete_product(self):
        product = Product.objects.get()
        response = self.client.delete(
            reverse('product-detail', kwargs={'pk': product.id}),
            format='json',
            follow=True)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

