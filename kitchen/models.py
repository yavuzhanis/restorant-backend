from django.db import models
from reservations.models import Reservation
from menu.models import MenuItem
from django.utils import timezone


class Order(models.Model):
    reservation = models.ForeignKey(
        Reservation, on_delete=models.CASCADE, related_name="orders"
    )
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    status = models.CharField(
        max_length=20,
        choices=[
            ("pending", "Beklemede"),
            ("preparing", "Hazırlanıyor"),
            ("ready", "Hazır"),
        ],
        default="pending",
    )
    created_at = models.DateTimeField(default=timezone.now)

    def total_price(self):
        item_price = self.menu_item.price if self.menu_item.price is not None else 0
        return (
            item_price * self.quantity
        )  # Menü öğesinin fiyatını miktarla çarparak toplam fiyatı hesaplar

    def __str__(self):
        return f"{self.menu_item.name} - {self.quantity} - {self.status}"
