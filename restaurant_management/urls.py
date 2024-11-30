from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter  # type:ignore
from reservations.views import ReservationViewSet
from kitchen.views import OrderViewSet
from billing.views import PaymentViewSet  # Billing modülü için view'i ekliyoruz

router = DefaultRouter()
router.register(r"reservations", ReservationViewSet)
router.register(r"payments", PaymentViewSet)  # Billing modülünü ekledik
urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("auth/", include("auth_app.urls")),
    path("menu/", include("menu.urls")),
    path("kitchen/", include("kitchen.urls")),
    path("end_of_day/", include("end_of_day.urls")),
]
