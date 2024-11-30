from django.urls import path
from . import views

urlpatterns = [
    path('orders/', views.kitchen_orders_view, name='kitchen_orders'),
]

app_name = 'kitchen'  # Uygulama adı (namespace)
