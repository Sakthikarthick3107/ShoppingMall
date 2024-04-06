from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})

class LoginResponseSerializer(serializers.Serializer):
    access = serializers.CharField()
    refresh = serializers.CharField()
    message = serializers.CharField()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username' , 'email' , 'first_name','last_name','password')
        extra_kwargs = {'password' : {'write_only' : True }}
        
    def validate_email(self,value):
        if User.objects.filter(email = value).exists():
            raise ValidationError('A user with this email already exists!')
        return value
    
    def create(self,validated_data):
        user = User.objects.create_user(**validated_data)
        return user