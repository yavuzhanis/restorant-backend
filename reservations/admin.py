from django.contrib import admin
from .models import Reservation

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'table_number', 'reservation_time', 'status')
    search_fields = ('customer_name', 'table_number')
    list_filter = ('status', 'reservation_time')

admin.site.register(Reservation, ReservationAdmin)
