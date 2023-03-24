from rest_framework import serializers
from .models import Transaction, Marketplace, PayoutType, Payout

class MarketplaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marketplace
        fields = ('id', 'mp_name')

class TransactionSerializer(serializers.ModelSerializer):
    mp_id = MarketplaceSerializer()
    class Meta:
        model = Transaction
        fields = ('id', 'date', 'mp_id', 'order_id', 'product_name', 'product_category', 'product_article', 
                    'quantity', 'selling_price', 'basic_price', 'notes', 'profit', 'margin')

class PayoutTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PayoutType
        fields = ('id', 'pay_type_name', 'pay_type_perc')

class PayoutSerializer(serializers.ModelSerializer):
    pay_type_id = PayoutTypeSerializer()
    class Meta:
        model = Payout
        fields = ('id', 'pay_date', 'pay_name', 'pay_type_id', 'pay_value')

class ProductSerializer(serializers.ModelSerializer):
    total_sales_by_product = serializers.IntegerField()
    class Meta:
        model = Transaction
        fields = ('id', 'product_article', 'total_sales_by_product')