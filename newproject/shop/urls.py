from django.urls import path,include

from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register('buy',views.ItemBuy)
router.register('sell',views.ItemSell)
router.register('shopadmin',views.ShopAdmin)

urlpatterns = [    
    path('',include(router.urls)),
]