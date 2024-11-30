from django.db import models
from django.db import models

class MenuCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2,null=False)
    category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE, related_name='items')

    def __str__(self):
        return f"{self.name} - {self.price} ₺"
