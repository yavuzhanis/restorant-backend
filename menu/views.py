from django.shortcuts import render
from rest_framework import viewsets  # type:ignore
from .models import MenuItem, MenuCategory
from .serializers import MenuItemSerializer, MenuCategorySerializer
from rest_framework.permissions import IsAuthenticated  # type:ignore


class MenuCategoryViewSet(viewsets.ModelViewSet):
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer
    permission_classes = [IsAuthenticated]


class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticated]
