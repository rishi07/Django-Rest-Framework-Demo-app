from django.shortcuts import render
from rest_framework import viewsets
from .models import Seller,Buyer,MyAdmin
from .serializers import SellerSerializer,BuyerSerializer,ShopAdminSerializer

class ItemBuy(viewsets.ModelViewSet):
	queryset = Buyer.objects.all()
	serializer_class = BuyerSerializer

class ItemSell(viewsets.ModelViewSet):
	queryset = Seller.objects.all()
	serializer_class = SellerSerializer

class ShopAdmin(viewsets.ModelViewSet):
	queryset = MyAdmin.objects.all()
	serializer_class = ShopAdminSerializer