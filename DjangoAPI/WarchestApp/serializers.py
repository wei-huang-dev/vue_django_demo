from rest_framework import serializers
from WarchestApp.models import WarchestData
from WarchestApp.models import UserData

class WarchestSerializer(serializers.ModelSerializer):
    class Meta:
        model=WarchestData 
        fields=('Id','Title', 'Field1', 'Field2', 'Field3', 'Field4', 'Field5', 'Date', 'photoFileName')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserData 
        fields=('username', 'email', 'first_name', 'last_name', 'password', 'last_login', 'date_joined', 'is_active', 'is_staff')