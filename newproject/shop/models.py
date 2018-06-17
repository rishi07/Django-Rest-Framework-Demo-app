from django.db import models

item_stocks = {"Laptop": 3, "Phone": 2, "Watch": 4, "Sippers": 5}
item_choices = ( ("Laptop", "Laptop"), ("Phone", "Phone"), ("Watch", "Watch"), ("Sippers", "Sippers") )	

class ItemDetails(models.Model):	

	item_name = models.CharField(max_length = 50, choices = item_choices)
	order_status = models.CharField(max_length = 50, default = "Submitting details")
 	