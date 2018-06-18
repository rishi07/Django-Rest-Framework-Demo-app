from rest_framework import serializers
from .models import Buyer,item_stocks,Seller,MyAdmin

class BuyerSerializer(serializers.ModelSerializer):
	
	def validate(self,data):
		qty = data['quantity']
		if(qty == 0):
			data['order_status'] = "Invalid quantity! Nothing to process"
			return data
		item_name = data['item_name']
		if item_stocks[item_name] > 0:
			if qty > item_stocks[item_name]:
				data['order_status'] = "Sorry! Less stock available than required"
			else:	 
				data['order_status'] = "Thank You! Order Placed Successfully"
				item_stocks[item_name]-=qty
		else:
			data['order_status'] = "Sorry! Out of Stock"
		return data
	
	class Meta:
		model = Buyer
		fields = ['id', 'url', 'item_name', 'quantity', 'order_status']
		read_only_fields = ['order_status'] 

class SellerSerializer(serializers.ModelSerializer):

	def validate(self,data):
		item_name = data['item_name']
		item_stocks[item_name] += data['add_value']
		data['item_stock_status'] = item_stocks[item_name]
		return data

	class Meta:
		model = Seller
		fields = ['id', 'url', 'item_name', 'add_value', 'item_stock_status']
		read_only_fields = ['item_stock_status']

class ShopAdminSerializer(serializers.ModelSerializer):

	def validate(self,data):
		item_name = data['item_name']
		item_stocks[item_name] += data['add_value']
		data['item_stock_status'] = item_stocks[item_name]
		qty = data['quantity']
		if(qty == 0):
			data['order_status'] = "Invalid quantity! Nothing to process"
			return data
		item_name = data['item_name']
		if item_stocks[item_name] > 0:
			if qty > item_stocks[item_name]:
				data['order_status'] = "Sorry! Less stock available than required"
			else:	 
				data['order_status'] = "Thank You! Order Placed Successfully"
				item_stocks[item_name]-=qty
		else:
			data['order_status'] = "Sorry! Out of Stock"
		data['item_stock_status'] = item_stocks[item_name]
		return data
	class Meta:
		model = MyAdmin
		fields = ['id', 'url', 'item_name', 'add_value', 'item_stock_status', 'quantity', 'order_status']
		read_only_fields = ['item_stock_status', 'order_status']
