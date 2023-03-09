from django import forms
from .models import Marketplace, Transaction, PayoutType, Payout
from django.conf import settings
 
# creating a form
class MarketplaceForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = Marketplace
 
        # specify fields to be used
        fields = [
            "mp_name",
        ]

class TransactionForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = Transaction
 
        # specify fields to be used
        fields = [
            "date",
            "mp_id",
            "order_id",
            "product_name",
            "product_category",
            "quantity",
            "selling_price",
            "basic_price",
            "notes"
        ]

class PayoutTypeForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = PayoutType
 
        # specify fields to be used
        fields = [
            "pay_type_name", "pay_type_perc"
        ]

class PayoutForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = Payout
 
        # specify fields to be used
        fields = [
            "pay_date", "pay_name", "pay_type_id", "pay_value"
        ]