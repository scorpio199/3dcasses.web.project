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
    product_article = models.CharField(max_length=200)
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

    def __product_article(self):
        return self.product_article

    def __quantity(self):
        return self.quantity

    def __selling_price(self):
        return self.selling_price

    def __basic_price(self):
        return self.basic_price

    def __notes(self):
        return self.notes

    def profit(self):
        return round(self.selling_price - (self.basic_price * self.quantity),2)
    
    def margin(self):
        profit = self.selling_price - (self.basic_price * self.quantity)
        return round((profit / self.selling_price) * 100,2)

class PayoutType(models.Model):
    pay_type_name = models.CharField(max_length=200)
    pay_type_perc = models.FloatField()

    def __pay_type_name(self):
        return self.pay_type_name

    def __pay_type_perc(self):
        return self.pay_type_perc

class Payout(models.Model):
    pay_date = models.DateField('date created')
    pay_name = models.CharField(max_length=200)
    pay_type_id = models.ForeignKey(PayoutType, to_field='id', on_delete=models.CASCADE)
    pay_value = models.DecimalField(max_digits=12, decimal_places=2)

    def __pay_date(self):
        return self.pay_date

    def __pay_name(self):
        return self.pay_name

    def __pay_type_id(self):
        return self.pay_type_id

    def __pay_value(self):
        return self.pay_value