from django.shortcuts import render
from .serializer import UserSerializer, UserLoginSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics



class Register(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Login(APIView):
    def post(self, request):
        serilaizer = UserLoginSerializer(data=request.data)
        if not serilaizer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        username = serilaizer.validated_data["username"]
        password = serilaizer.validated_data["password"]
        user = authenticate(username=username, password=password)
        if user is None:
            return Response({"error:invalid password or username"})

        login(request, user)
        return Response(status=status.HTTP_200_OK)


class Logout(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)