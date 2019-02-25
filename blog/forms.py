from django import forms
from . import models

class Comment(forms.ModelForm):
	class Meta:
		model = models.Comment
		fields = ['author', 'comment']
