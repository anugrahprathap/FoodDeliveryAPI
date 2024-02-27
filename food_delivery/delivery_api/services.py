class PriceCalculator:
    @staticmethod
    def calculate_price(organization_id, zone, total_distance, item_type):
        base_distance = 5  # Base distance
        base_price = 10  # Base price
        perishable_price_per_km = 1.5  # Per km price for perishable items
        non_perishable_price_per_km = 1  # Per km price for non-perishable items
        
        # Calculate total price
        if total_distance <= base_distance:
            total_price = base_price
        else:
            if item_type == 'perishable':
                price_per_km = perishable_price_per_km
            else:
                price_per_km = non_perishable_price_per_km
            total_price = base_price + (total_distance - base_distance) * price_per_km
        
        return total_price