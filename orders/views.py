from rest_framework import viewsets
from orders.models import Order
from .serializers import OrderSerializer
from django.shortcuts import render
from .forms import OrderForm

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

def create_order(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            # Process the form and save the order
            form.save()
            # Redirect or render a success template
    else:
        form = OrderForm()

    return render(request, 'orders/create_order.html', {'form': form})

