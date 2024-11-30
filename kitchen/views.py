from django.http import JsonResponse
from rest_framework import viewsets #type:ignore
from .models import Order
from .serializers import OrderSerializer

# API üzerinden Order'ları almak için ViewSet
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

# Geleneksel view fonksiyonu ile siparişleri JSON formatında almak
def kitchen_orders_view(request):
    orders = Order.objects.all()  # Tüm siparişleri al
    orders_data = [
        {
            "id": order.id,
            "customer": order.customer.username,
            "status": order.status,
            "created_at": order.created_at,
        }
        for order in orders
    ]
    return JsonResponse({"orders": orders_data})

