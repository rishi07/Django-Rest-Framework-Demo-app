from django.shortcuts import render
from rest_framework import viewsets
from .models import ItemDetails
from .serializers import ItemSerializer

class ItemView(viewsets.ModelViewSet):
	queryset = ItemDetails.objects.all()
	serializer_class = ItemSerializer
