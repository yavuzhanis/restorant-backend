from django.contrib import admin
from django.contrib import admin
from .models import MenuItem, MenuCategory

# Menü Kategorisi Modelini Admin Paneline Ekleyin
@admin.register(MenuCategory)
class MenuCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # Kategorileri listelemek için alanlar
    search_fields = ('name',)  # Kategori adına göre arama yapma

# Menü Öğesi Modelini Admin Paneline Ekleyin
@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category')  # Menü öğelerini listelemek için alanlar
    list_filter = ('category',)  # Kategoriye göre filtreleme
    search_fields = ('name',)  # Menü öğesi adına göre arama yapma
