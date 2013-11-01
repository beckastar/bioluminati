# copied from django.contrib.auth.forms.UserCreationForm, but changed to use our custom User.
from django import forms
from django.utils.translation import ugettext as _
from biocore.models import User

class UserCreationForm(forms.ModelForm):
    """
    A form that creates a user, with no privileges, from the given username and
    password.
    """
    error_messages = {
        'duplicate_username': _("A user with that username already exists."),
        'password_mismatch': _("The two password fields didn't match."),
    }
    username   = forms.RegexField(label=_("Username"), max_length=30,
        regex=r'^[\w.@+-]+$',
        help_text=_("Required. 30 characters or fewer. Letters, digits and "
                      "@/./+/-/_ only."),
        error_messages={
            'invalid': _("This value may contain only letters, numbers and "
                         "@/./+/-/_ characters.")})
    email      = forms.EmailField(label=_("E-mail"))
    first_name = forms.CharField(label=_("First name"))
    last_name = forms.CharField(label=_("Last name"))
    password1  = forms.CharField(label=_("Password"),
        widget=forms.PasswordInput)
    password2  = forms.CharField(label=_("Password confirmation"),
        widget=forms.PasswordInput,
        help_text=_("Enter the same password as above, for verification."))

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name")

    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            User._default_manager.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(
            self.error_messages['duplicate_username'],
            code='duplicate_username',
        )

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

# #this file allows you to add fields to form
# from django import forms
# from django.core.exceptions import ValidationError

# from contacts.models import Contact 
# from contacts.models import Address

# from django.forms.models import inlineformset_factory

# #creating new model form 
# class ContactForm(forms.ModelForm):
# #allows you to get confirmation of email address
# 	confirm_email = forms.EmailField(
# 		"Confirm email",
# 		required = "True",
# 		)
# 	class Meta:
# 		model = Contact

# 	def __init__(self, *args, **kwargs):

# 		if kwargs.get('instance'):

# 			email = kwargs['instance'].email
# 			kwargs.setdefault('initial', {})['confirm_email']=email

# 		return super(ContactForm, self).__init__(*args, **kwargs)
# 		#clean method validates all the fields available in cleaned data dictionary
# 		#fields MUST BE VALIDATED
# 	def clean(self):

# 		if(self.cleaned_data.get('email')!=
# 			self.cleaned_data('confirm_email')):

# 			raise ValidationError(
# 				"Email addresses must match."
# 			)
# 		return self.cleaned_data
# # inlineformset_factory creates a Class from a parent model (Contact)
# # to a child model (Address)

# #factory functions to create class for you
# ContactAddressFormSet = inlineformset_factory(
#     Contact,
#     Address,
# )
