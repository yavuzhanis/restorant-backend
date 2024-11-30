from rest_framework.permissions import BasePermission #type:ignore

class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Yönetici').exists()

class IsEmployeeUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Çalışanlar').exists()
