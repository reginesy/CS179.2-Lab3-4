from django.db import models

class User (models.Model):
	email = models.EmailField(max_length=100)
	first_name = models.CharField(max_length=42)
	last_name = models.CharField(max_length=42)
	address = models.CharField(max_length=100)

	def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

class Product(models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField()
	price = models.DecimalField(max_digits=10, decimal_places=2)

	def __str__(self):
		return self.name

class Cart(models.Model):
	cart_code = models.CharField(max_length=42)
	product = models.ManyToManyField (Product)
	total_price = models.DecimalField(max_digits=10, decimal_places=2)
	paid = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now = True)
    
    def __str__(self):
    	return self.cart_code

# Each user would have an email, first name, last name, and shipping address.

# Each cart would have a cart_code, total price, one or more products, and a way to know if the cart has been paid

# Each product would have a price, name, and description.