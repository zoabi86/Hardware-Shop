from django.core.management.base import BaseCommand
from products.models import Product, Category

class Command(BaseCommand):
    help = 'Updates categories for products'

    def handle(self, *args, **kwargs):
        valid_category = Category.objects.first()  # or your logic for a valid category
        for product in Product.objects.all():
            product.category = None #valid_category  # or None
            product.save()

        self.stdout.write(self.style.SUCCESS('Successfully updated categories for products'))

