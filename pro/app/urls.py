from django.urls import path
from .views import serial_view

urlpatterns = [
    path('item/',serial_view.as_view(),name='serial_view'),
]