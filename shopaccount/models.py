from django.db import models

class Marketplace(models.Model):
    mp_name = models.CharField(max_length=200)

    def __str__(self):
        return self.mp_name

class Transaction(models.Model):
    date = models.DateField('date created')
    mp_id =  models.ForeignKey(Marketplace, to_field='id', on_delete=models.CASCADE)
    order_id = models.CharField(max_length=200)
    product_name = models.CharField(max_length=200)
    product_category = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)
    selling_price = models.DecimalField(max_digits=12, decimal_places=2)
    basic_price = models.DecimalField(max_digits=12, decimal_places=2)
    notes = models.TextField(max_length=500)
    
    def __date(self):
        return self.date

    def __mp_id(self):
        return self.mp_id

    def __order_id(self):
        return self.order_id

    def __product_name(self):
        return self.product_name

    def __product_category(self):
        return self.product_category

    def __quantity(self):
        return self.quantity

    def __selling_price(self):
        return self.selling_price

    def __basic_price():
        return self.basic_price

    def __notes(self):
        return self.notes

    def profit(self):
        return round(self.selling_price - (self.basic_price * self.quantity),2)
    