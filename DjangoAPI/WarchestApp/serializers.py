from rest_framework import serializers
from WarchestApp.models import WarchestData

class WarchestSerializer(serializers.ModelSerializer):
    class Meta:
        model=WarchestData 
        fields=('Id','Title', 'Field1', 'Field2', 'Field3', 'Field4', 'Field5', 'Date', 'photoFileName')