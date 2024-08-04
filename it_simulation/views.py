from django.shortcuts import render
from rest_framework import generics
from .models import ITService
from .serializers import ITServiceSerializer

class ITServiceList(generics.ListCreateAPIView):
    queryset = ITService.objects.all()
    serializer_class = ITServiceSerializer

class ITServiceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ITService.objects.all()
    serializer_class = ITServiceSerializer


# Create your views here.
