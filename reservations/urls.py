from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter #type:ignore
from reservations.views import ReservationViewSet

router = DefaultRouter()
router.register(r'reservations', ReservationViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
