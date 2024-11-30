from django.shortcuts import render
from rest_framework import generics  # type:ignore
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny  # type:ignore
from rest_framework.response import Response  # type:ignore
from rest_framework import status  # type:ignore


class RegisterView(generics.CreateAPIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")
        user = User.objects.create_user(username=username, password=password)
        return Response(
            {"message": "User created successfully"}, status=status.HTTP_201_CREATED
        )
