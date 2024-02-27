# delivery_api/urls.py

from django.urls import path
from .views import DeliveryCostView

urlpatterns = [
    path('delivery_cost/', DeliveryCostView.as_view(), name='calculate_delivery_cost'),
]
