from django.shortcuts import render
from .models import Place 
from . serializers import PlaceSerializer 
from django_filters.rest_framework import DjangoFilterBackend 
from rest_framework import generics, filters
# Create your views here.


class PlaceList(generics.ListAPIView): 

    queryset = Place.objects.all() 
    serializer_class = PlaceSerializer 
    filter_backends = [DjangoFilterBackend , filters.SearchFilter] 
    filterset_fields = ['category']  
    search_fields = ['name', 'description']
