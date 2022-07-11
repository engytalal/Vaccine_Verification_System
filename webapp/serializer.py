from . models import user , employee
from rest_framework import serializers
from django.contrib.auth.models import User
class userserializer(serializers.ModelSerializer):
    class Meta:
        model=user
        fields='__all__'
class employeeserializer(serializers.ModelSerializer):
    class Meta:
        model=employee
        fields='__all__'
class adminserializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'

