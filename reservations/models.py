from django.db import models

# Create your models here.
from django.db import models

class Reservation(models.Model):
    customer_name = models.CharField(max_length=100)          # Müşteri adı
    table_number = models.IntegerField()                      # Masa numarası
    reservation_time = models.DateTimeField()                 # Rezervasyon zamanı
    status = models.CharField(                                # Rezervasyon durumu
        max_length=20,
        choices=[
            ('pending', 'Beklemede'),
            ('confirmed', 'Onaylandı'),
            ('completed', 'Tamamlandı'),
        ],
        default='pending'
    )

    def __str__(self):
        return f"{self.customer_name} - Masa {self.table_number} - {self.status}"
