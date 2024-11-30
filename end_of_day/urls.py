# end_of_day/urls.py
from django.urls import path
from .views import daily_report_view  # Sadece gerekli olan fonksiyonu import edin

urlpatterns = [
    path('daily-report/', daily_report_view, name='daily_report'),
]
