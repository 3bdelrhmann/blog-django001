from django import forms
from .models import comments
class Newcomment(forms.ModelForm):

	class Meta:
		model = comments
		fields = ('name','email','body')