import json

from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from rest_framework_jwt.settings import api_settings

from rest_framework import viewsets, permissions, status, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from src.api.serializers import CreateUserSerializer, UserSerializer, LoginUserSerializer

from knox.models import AuthToken


class UserCreate(generics.GenericAPIView):
    """ 
    Creates the user. 
    """

    serializer_class = CreateUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)
        })


class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)
        })


class UserAPI(generics.RetrieveAPIView):
    # permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

@csrf_exempt
def CheckEmail(request):
    if request.method == 'POST':
        email = request.GET['email']
        user = User.objects.filter(email=email).count()
        if user > 0:
            result = True
        else:
            result = False
        return JsonResponse({'result':result, 'request':email})


@csrf_exempt
def CheckUsername(request):
    if request.method == 'POST':
        username = request.GET['username']
        user = User.objects.filter(username=username).count()
        if user > 0:
            result = True
        else:
            result = False
        return JsonResponse({'result':result, 'request':username})