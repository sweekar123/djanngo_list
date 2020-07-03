from django.db import models

# Create your models here.
 	
class people(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	username = models.CharField(max_length=100)
	email = models.EmailField(max_length=100)
	password_1 = models.CharField(max_length=100)
	password_2 = models.CharField(max_length=100)
	address = models.CharField(max_length=100)
	city = models.CharField(max_length=100)

	def __str__(self):
		return self.first_name
 			 	