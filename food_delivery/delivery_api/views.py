# delivery_api/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from .services import PriceCalculator
from .models import Pricing,Item
class DeliveryCostView(APIView):
    
    def post(self, request):
        data = request.data
        organization_id = data.get('organization_id')
        zone = data.get('zone')
        total_distance = data.get('total_distance')
        item_id = data.get('item_id')  # Change to get item_id instead of item_type

        # Fetch the Item instance based on item_id
        try:
            item = Item.objects.get(pk=item_id)
        except Item.DoesNotExist:
            return Response({'error': 'Item not found'}, status=400)

        # Get the item type from the Item instance
        item_type = item.type

        total_price = PriceCalculator.calculate_price(organization_id, zone, total_distance, item_type)

        if total_price is None:
            return Response({'error': 'Unable to calculate price'}, status=400)
        
        # Creating a new Pricing object
        pricing = Pricing(
            organization_id=organization_id,
            item_id=item_id,  # You need to specify the item_id
            zone=zone,
            price=total_price
        )
        pricing.save()

        return Response({'total_price': total_price})
