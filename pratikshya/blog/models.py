from django.db import models
from django.urls import reverse

# Create your models here.
class Journal(models.Model):
	username = models.CharField(max_length=100)
	title = models.CharField(max_length=200)
	description = models.TextField(blank=False)
	content = models.TextField(blank=False)
	image_1 = models.ImageField(upload_to='media', height_field=120, width_field=120, blank=True)
	image_2 = models.ImageField(upload_to='media', height_field=120, width_field=120, blank=True)
	visibility = models.BooleanField(default=False)


	def get_absolute_url(self):
		return reverse("blog:journal-detail",kwargs={ "id" : self.id })
