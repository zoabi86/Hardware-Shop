from django.test import TestCase
from django.contrib.auth.models import User
from products.models import Product, Category
from orders.models import Order, OrderItem

class OrderTestCase(TestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='12345')
        Category.objects.create(name="Electronics")
        
        # Create some products
        self.product1 = Product.objects.create(name='Product 1', barcode="123456789012", price=10.00, stock_count=5, category=Category.objects.get(name="Electronics"))
        self.product2 = Product.objects.create(name='Product 2', barcode="223222672212", price=15.00, stock_count=3, category=Category.objects.get(name="Electronics"))

        # Create an order
        self.order = Order.objects.create(user=self.user)

        # Add products to the order with quantities
        OrderItem.objects.create(order=self.order, product=self.product1, quantity=2)
        OrderItem.objects.create(order=self.order, product=self.product2, quantity=1)

    def test_order_quantity_vs_stock_count(self):
        for item in self.order.order_items.all():
            self.assertLessEqual(item.quantity, item.product.stock_count, 
                                 f"Quantity of {item.product.name} in the order exceeds available stock.")

