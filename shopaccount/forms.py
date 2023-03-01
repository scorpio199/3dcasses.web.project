from django import forms
from .models import Marketplace, Transaction
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

        #labels = {
        #    'title': _('Judul'),
        #    'description': _('Deskripsi'),
        #    'status': _('Status')
        #}

        #error_messages = {
        #    'title': {
        #        'required': _("Judul harus diisi."),
        #    },
        #    'description': {
        #        'required': _("Deskripsi harus diisi."),
        #    },
        #}

        widgets = {
            #'prename': TextInput(attrs={"class": "form-control form-group", "required:": "", "placeholder": "Vorname*", "style": "max-width: 800px; margin-left: auto; margin-right: auto;"}),
            #'surname': TextInput(attrs={"class": "form-control dragArea col-md col-sm-12 form-group mb-3", "required:": "", "placeholder": "Nachname*", "style": "max-width: 800px; margin-left: auto; margin-right: auto;"}),
            #'punkte': TextInput(attrs={"class": "form-control dragArea col-md col-sm-12 form-group mb-3", "required:": "", "placeholder": "Aktien Anzahl*", "style": "max-width: 800px; margin-left: auto; margin-right: auto;"}),
            'date': forms.DateInput(format=settings.DATE_INPUT_FORMATS, attrs={'class': 'datepicker', 'type': 'date'})
        }