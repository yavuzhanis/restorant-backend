from rest_framework import serializers # type:ignore
from .models import Reservation

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'
