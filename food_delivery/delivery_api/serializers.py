# delivery_api/serializers.py

from rest_framework import serializers
from .models import Organization, Pricing

class PricingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pricing
        fields = '__all__'
