from django.db import models

class User (models.Model):
	email = models.EmailField(max_length=75)
	first_name = models.CharField(max_length=42)
	last_name = models.CharField(max_length=42)
	address = models.CharField(max_length=42)

class Product(models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField()


class CartItem(models.Model):
    cart = models.ForeignKey("Cart")
    item = models.ForeignKey(Product)

class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)
    items = models.ManyToManyField(Product, through=CartItem)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, )
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, )

    def __unicode__(self):
        return str(self.id)
# Create your models here.
# Each user would have an email, first name, last name, and shipping address.

# Each cart would have a cart_code, total price, one or more products, and a way to know if the cart has been paid

# Each product would have a price, name, and description.

# While this basic setup is ok, we also want to be able to query for only paid carts and unpaid carts.
# Also, I want to be able to know when the cart was created and when the cart has been updated.
