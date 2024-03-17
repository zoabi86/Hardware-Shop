from django.contrib import admin
from .models import Order, OrderItem
from django import forms
# Other imports if necessary

class OrderAdminForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'  # Include all necessary fields

    # Add custom fields or widgets if necessary

# Inline admin for OrderItem
class OrderItemInline(admin.TabularInline):  # or admin.StackedInline
    model = OrderItem
    extra = 1

# Admin for Order
class OrderAdmin(admin.ModelAdmin):
    form = OrderAdminForm
    inlines = [OrderItemInline]
    # ... other configurations ...

# Register Order with its custom admin
admin.site.register(Order, OrderAdmin)

# Optionally, register OrderItem if needed separately
# admin.site.register(OrderItem)


