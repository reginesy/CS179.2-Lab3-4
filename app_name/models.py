from django.db import models

class InfoClass (models.Model):

class User (InfoClass):
	email = models.EmailField(max_length=100)
	first_name = models.CharField(max_length=42)
	last_name = models.CharField(max_length=42)
	address = models.CharField(max_length=100)

class Product(InfoClass):
	name = models.CharField(max_length=50)
	description = models.TextField()
	price = models.FloatField()


class Cart(InfoClass):
	cart_code = models.CharField(max_length=42)
	product = models.ManyToManyField (Product)
	paid = models.BooleanField(default=1)
    
    def total_price(self, price):
    	product = Product()
    	price = price + product.price

    def __unicode__(self):
        return str(self.id)

    def is_active(self):
        return bool(self.active_status)

# Each user would have an email, first name, last name, and shipping address.

# Each cart would have a cart_code, total price, one or more products, and a way to know if the cart has been paid

# Each product would have a price, name, and description.