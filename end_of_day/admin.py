from django.contrib import admin
from .models import EndOfDayReport

class EndOfDayReportAdmin(admin.ModelAdmin):
    list_display = ('date', 'total_orders', 'total_sales', 'total_payments', 'total_completed_orders')  #! Listelemede gösterilecek alanlar
    search_fields = ('date',)
    list_filter = ('date',)

admin.site.register(EndOfDayReport, EndOfDayReportAdmin)
