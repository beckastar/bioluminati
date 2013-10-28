#this file allows you to add fields to form
from django import forms
from django.core.exceptions import ValidationError

from contacts.models import Contact 
from contacts.models import Address

from django.forms.models import inlineformset_factory

#creating new model form 
class ContactForm(forms.ModelForm):
#allows you to get confirmation of email address
	confirm_email = forms.EmailField(
		"Confirm email",
		required = "True",
		)
	class Meta:
		model = Contact

	def __init__(self, *args, **kwargs):

		if kwargs.get('instance'):

			email = kwargs['instance'].email
			kwargs.setdefault('initial', {})['confirm_email']=email

		return super(ContactForm, self).__init__(*args, **kwargs)
		#clean method validates all the fields available in cleaned data dictionary
		#fields MUST BE VALIDATED
	def clean(self):

		if(self.cleaned_data.get('email')!=
			self.cleaned_data('confirm_email')):

			raise ValidationError(
				"Email addresses must match."
			)
		return self.cleaned_data
# inlineformset_factory creates a Class from a parent model (Contact)
# to a child model (Address)

#factory functions to create class for you
ContactAddressFormSet = inlineformset_factory(
    Contact,
    Address,
)
