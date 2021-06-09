from django import forms

from form.models import Form

class SubmitForm(forms.ModelForm):
	class Meta:
		model= Form
		fields= '__all__'
