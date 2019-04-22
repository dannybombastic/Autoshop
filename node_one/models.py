# Create your models here.
from django.db import models
from django.contrib.gis.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import User, Group
from rest_framework import serializers, exceptions

class UserSerializer(serializers.ModelSerializer):
     

    class Meta:
        model = User
        fields = ('id', 'username',)


# Create your models here.



class WorldMenbers(models.Model):
    # Regular Django fields corresponding to the attributes in the
    # world borders shapefile.
    name = models.CharField(max_length=50, verbose_name='Nombre')
    image = models.ImageField(verbose_name='Imagen', blank=True, upload_to="pics/")
    poly = models.PolygonField()
    point = models.PointField()



    def __str__(self):
      return self.name


class MenbersPoint(models.Model):
    # Regular Django fields corresponding to the attributes in the
    # world borders shapefile.
    name = models.CharField(max_length=50, verbose_name='Addres')
    point = models.PointField()
     
    def __str__(self):
      return self.name