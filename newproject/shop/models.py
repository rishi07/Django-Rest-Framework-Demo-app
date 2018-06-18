from django.db import models

item_stocks = {"Laptop": 0, "Phone": 0, "Watch": 0, "Sippers": 0}
item_choices = ( ("Laptop", "Laptop"), ("Phone", "Phone"), ("Watch", "Watch"), ("Sippers", "Sippers") )	

class Buyer(models.Model):	

	item_name = models.CharField(max_length = 50, choices = item_choices)
	quantity = models.IntegerField(default = 1)
	order_status = models.CharField(max_length = 50, default = "Submitting details")

 	
class Seller(models.Model):
	
	item_name = models.CharField(max_length = 50, choices = item_choices)
	add_value = models.IntegerField(default = 0)
	item_stock_status = models.IntegerField(default = 0)

class MyAdmin(models.Model):

	item_name = models.CharField(max_length = 50, choices = item_choices)
	quantity = models.IntegerField(default = 1)
	add_value = models.IntegerField(default = 0)
	order_status = models.CharField(max_length = 50, default = "Submitting details")
	item_stock_status = models.IntegerField(default = 0)

