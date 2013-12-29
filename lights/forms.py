from django.db import models
from django.forms import ModelForm
from ourcrestmont.itaco.models import *

class AttendanceForm(forms.ModelForm):
	camping_in_2014 = forms.BooleanField()

	def __init__(self):
		if check_something():
			self.fields['camping_in_2014'].initial = True

	class Meta:
		model = Settings
      	# exclude = ('field1','field2','field3',)