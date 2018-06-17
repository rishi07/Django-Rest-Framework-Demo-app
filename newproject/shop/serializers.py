from rest_framework import serializers
from .models import ItemDetails,item_stocks

class ItemSerializer(serializers.ModelSerializer):
	
	def validate(self,data):
		item_name = data['item_name']
		if item_stocks[item_name] > 0:
			data['order_status'] = "Thank You! Order Placed Successfully"
			item_stocks[item_name]-=1
		else:
			data['order_status'] = "Sorry! Out of Stock"
		return data
	
	class Meta:
		model = ItemDetails
		fields = ['id', 'url', 'item_name', 'order_status']
		read_only_fields = ['order_status'] 
		# print(fields.item_name)