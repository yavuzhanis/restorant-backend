from django.urls import path, include
from rest_framework.routers import DefaultRouter #type:ignore
from .views import MenuItemViewSet, MenuCategoryViewSet

router = DefaultRouter()
router.register(r'menu-items', MenuItemViewSet)
router.register(r'menu-categories', MenuCategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
