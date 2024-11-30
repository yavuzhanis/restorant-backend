from django.db import models
from reservations.models import Reservation


class Payment(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    payment_method = models.CharField(
        max_length=20,
        choices=[("cash", "Nakit"), ("credit_card", "Kredi Kartı"), ("online", "Online")],
        default="cash",
    )
    payment_date = models.DateTimeField(auto_now_add=True)

    @property
    def total_price(self):
        total = 0
        for order in self.reservation.orders.all():
            total += order.total_price()
        return total

    def __str__(self):
        return f"{self.reservation.customer_name} - {self.total_price} - {self.payment_method}"
