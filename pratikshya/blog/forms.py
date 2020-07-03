from .models import Journal
from django import forms



class Journalform(forms.ModelForm):
	class Meta:
		model = Journal
		fields = [
		   'username',
           'title',
           'description',
           'content',
           'image_1',
           'image_2',
           'visibility',
           ]
           
