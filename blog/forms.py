from django import forms
from . import models

class Comment(forms.ModelForm):

	class Meta:
		model = models.Comment
		fields = ['author', 'comment']
		widgets = {
			'author':forms.TextInput(attrs = {'placeholder' : 'Your Name'}),
			'comment':forms.Textarea(attrs = {'placeholder' : 'Your Comment', 'rows' : 5, 'class' : 'form_style' }),
		}
		labels = {
			'author' : (''),
			'comment' : ('')
		}