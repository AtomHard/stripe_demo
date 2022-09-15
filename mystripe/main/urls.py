from django.urls import path

from main.views import *

urlpatterns = [
    path('', index, name='home'),
    path('item/<int:itemid>/', item_detail, name='item_detail'),
    path('buy/<int:itemid>/', buy_item, name='buy_item'), #/create-checkout-session
    path('success/', success, name='success'),
    path('cancel/', cancel, name='cancel'),
]

