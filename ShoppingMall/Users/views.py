from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.response import Response
from .serializers import UserSerializer , LoginSerializer , LoginResponseSerializer
from rest_framework.views import APIView
from rest_framework import status
from drf_spectacular.utils import extend_schema
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.tokens import AccessToken,RefreshToken
from django.contrib.auth import authenticate , get_user_model

# Create your views here.

User = get_user_model()

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls,user):
        token = super().get_token(user)
        token['username'] = user.username
        token['email'] = user.email
        return token
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@extend_schema(request=LoginSerializer, responses={200: LoginResponseSerializer})
class LoginView(APIView):
    def post(self,request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():   
        
            user = authenticate(**serializer.validated_data)
        
            if not user:
                return Response({'error' : 'Invalid Credentials'} , status=status.HTTP_400_BAD_REQUEST)
            else:
                access_token = AccessToken.for_user(user)
                refresh_token = RefreshToken.for_user(user)
                access_token['username'] = user.username
                return Response({
                'access_token' : str(access_token) , 
                'refresh_token': str(refresh_token),
                'message' : 'Logged in Successfully'
                },status = status.HTTP_200_OK)


@extend_schema(request=UserSerializer, responses={201: UserSerializer})

class RegisterView(APIView):
    def get(self,request , id=None):
        if id is not None:
            individual = User.objects.get(id=id)
            serializer = UserSerializer(individual)
            return Response(serializer.data)
        users = User.objects.all()
        serializer = UserSerializer(users , many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'data':serializer.data,
                'message' : 'Registered Successfully'
                } , status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)