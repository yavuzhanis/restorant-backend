from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('reservation', 'menu_item', 'quantity', 'status', 'total_price')  # Total Price'ı ekliyoruz

admin.site.register(Order, OrderAdmin)
