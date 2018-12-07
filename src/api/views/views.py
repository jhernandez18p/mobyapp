import json

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from rest_framework_jwt.settings import api_settings

from rest_framework import viewsets, permissions, status, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from src.api.serializers import CreateUserSerializer, UserSerializer, LoginUserSerializer, ArticleSerializer
from src.ventas.models import Line, SubLine, Color, \
    Type, Provider, Brands, Department, Category, Article

from knox.models import AuthToken

@csrf_exempt
def UpdateViews(request):
    if request.method == 'GET':
        # product = request.GET['slug']
        # if Article.objects.all().get(slug=product):
        result = True
    else:
        result = False
    print(result)
    return JsonResponse({'result':result, 'request':'product'})


class UserCreate(generics.CreateAPIView):
    """ 
    Creates the user. 
    """

    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer



class LoginAPI(APIView):
    permission_classes = ()
    
    def post(self, request,):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        
        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response({"error": "Credenciales incorrectas"}, status=status.HTTP_400_BAD_REQUEST)
        
# class LoginAPI(generics.GenericAPIView):
#     serializer_class = LoginUserSerializer

#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data
#         return Response({
#             "user": UserSerializer(user, context=self.get_serializer_context()).data,
#             "token": AuthToken.objects.create(user)
#         })


class UserAPI(generics.RetrieveAPIView):
    # permission_classes = [permissions.IsAuthenticated, ]
    # serializer_class = UserSerializer
    serializer_class = LoginUserSerializer

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
