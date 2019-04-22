from django.contrib.auth.models import User, Group
from rest_framework import serializers, exceptions
from django.contrib.gis.db import models
from django.contrib.auth import authenticate, login
from .models import WorldMenbers, MenbersPoint
from rest_framework_gis.serializers import GeoFeatureModelSerializer




# Create your models here.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        #fields = ('url', 'username', 'email', 'groups','password')
   
    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user 
    
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class CordenateSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
         model = WorldMenbers
         geo_field = 'poly'
         fields = ('name','image','poly','point')


class CordenateMenbersSerializer(GeoFeatureModelSerializer):
     class Meta:
     
         model = MenbersPoint
         geo_field = 'point'
         fields = '__all__'

class LoginSerializer(serializers.Serializer):
     class Meta:
         model = User
         fields = '__all__'
 
     username = serializers.CharField()
     password = serializers.CharField()
 
     def validate(self,data):
         username = data.get("username","")
         password = data.get("password","")
         if username and password:
             user = authenticate(username = username, password = password)
             if user:
                 if user.is_active:
                     data["user"] = user
                 else:
                     msg = 'User is deactivate'
                     raise exceptions.ValidationError(msg)    
             else:
                 msg = 'Unable to login with credentials'   
                 raise exceptions.ValidationError(msg) 
         else:
             msg = 'Must provide username and password'
             raise exceptions.ValidationError(msg)    
         return data
   
 