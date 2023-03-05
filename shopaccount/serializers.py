from rest_framework import serializers
from .models import Transaction, Marketplace

class MarketplaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marketplace
        fields = ('id', 'mp_name')

class TransactionSerializer(serializers.ModelSerializer):
    mp_id = MarketplaceSerializer()
    class Meta:
        model = Transaction
        fields = ('id', 'date', 'mp_id', 'order_id', 'product_name', 'product_category', 
                    'quantity', 'selling_price', 'basic_price', 'notes', 'profit', 'margin')