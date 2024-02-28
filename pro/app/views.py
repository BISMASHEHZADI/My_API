from django.shortcuts import render
from .models import My_Model
from .serializer import My_Serializer
from rest_framework import generics

# Create your views here.


class serial_view(generics.ListCreateAPIView):
    queryset = My_Model.objects.all()
    serializer_class = My_Serializer
    