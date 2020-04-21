from django.db import models

# Create your models here.

class Product(models.Model):
	img = models.CharField(max_length=200)
	status = models.CharField(max_length=200)
	status_text = models.CharField(max_length=200)
	name = models.CharField(max_length=200, primary_key=True)
	price = models.CharField(max_length=200)

	def __str__(self):
		return f'{self.name}:{self.price}'