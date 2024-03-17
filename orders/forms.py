from django import forms
from .models import Order, Product

class OrderForm(forms.ModelForm):
    products = forms.ModelMultipleChoiceField(
        queryset=Product.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Order
        fields = ['user', 'products']

