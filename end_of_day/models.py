from django.db import models
from django.utils import timezone
from kitchen.models import Order
from billing.models import Payment

class EndOfDayReport(models.Model):
    date = models.DateField(default=timezone.now)
    total_orders = models.PositiveIntegerField(default=0)
    total_sales = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_payments = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_completed_orders = models.PositiveIntegerField(default=0)

    def generate_report(self):
        today = self.date
        orders_today = Order.objects.filter(created_at__date=today)
        payments_today = Payment.objects.filter(payment_date__date=today)

        # Tamamlanan siparişler
        completed_orders = orders_today.filter(status='ready')

        # Toplam sipariş sayısı
        self.total_orders = orders_today.count()

        # Toplam satış (siparişlerin toplam fiyatı)
        self.total_sales = sum(order.total_price() for order in orders_today)

        # Toplam ödeme (`Payment` modelindeki `total_price` ile)
        self.total_payments = sum(payment.total_price for payment in payments_today)

        # Tamamlanan sipariş sayısı
        self.total_completed_orders = completed_orders.count()

    def save(self, *args, **kwargs):
        self.generate_report()  # Rapor kaydedilmeden önce hesaplanacak
        super(EndOfDayReport, self).save(*args, **kwargs)

    def __str__(self):
        return f"End of Day Report for {self.date} - Total Sales: {self.total_sales} - Total Payments: {self.total_payments}"
