from django.contrib import admin
from .models import Buyer,Seller,MyAdmin

admin.site.register(Buyer)
admin.site.register(Seller)
admin.site.register(MyAdmin)