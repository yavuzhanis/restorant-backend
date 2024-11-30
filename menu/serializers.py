from rest_framework import serializers #type:ignore
from .models import MenuItem, MenuCategory

class MenuCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuCategory
        fields = ['id', 'name']

class MenuItemSerializer(serializers.ModelSerializer):
    category = MenuCategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=MenuCategory.objects.all(), source='category', write_only=True
    )

    class Meta:
        model = MenuItem
        fields = ['id', 'name', 'description', 'price', 'category', 'category_id']
