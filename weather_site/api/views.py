from django.shortcuts import render
from rest_framework import generics
from .serializers import CitySerializer
from .models import City

# Create your views here.
class CityView(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
