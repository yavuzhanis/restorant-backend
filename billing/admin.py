from django.contrib import admin
from .models import Payment

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('reservation', 'payment_method', 'payment_date', 'total_price')  # Total Price'ı ekliyoruz
    search_fields = ('payment_method',)
    list_filter = ('payment_method', 'payment_date')

admin.site.register(Payment, PaymentAdmin)
