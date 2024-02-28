from .models import My_Model
from rest_framework import serializers


class My_Serializer(serializers.ModelSerializer):
    class Meta:
        model = My_Model
        fields = ['title','product_name']
