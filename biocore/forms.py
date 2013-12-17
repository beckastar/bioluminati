# copied from django.contrib.auth.forms.UserCreationForm, but changed to use our custom User.
from django import forms
from django.utils.translation import ugettext as _
from biocore.models import User, Travel, Meal, MealSignup
from django.utils import timezone
import datetime

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

class TravelFrom(forms.Form):
    def __init__(self, *args, **kwargs):
        super(TravelFrom, self).__init__(*args, **kwargs)
        self.fields['extra_thing'] = forms.BooleanField(label ="dynamic field", required = True,
                                            initial = False)

    from_city = forms.ChoiceField(required=True,
                                    choices=Travel.CITY_CHOICES)
    other_place = forms.CharField(label = _("You're not from around here, are ya?  Where are you traveling from?"))

    helping_with_setup = forms.BooleanField(label ="Check here if you'll be helping us with setup (requires early arrival ticket).",
                                            required = True,
                                            initial = False)
    helping_with_exedus = forms.BooleanField(label = "Check here if you will be helping with exedus.",
                                                required =True,
                                                initial = False)
    arrival_date = forms.ChoiceField(required=True,
                                        choices=User.DATES_2014)
    #first_meal = forms.ChoiceField(required = True, choices = User_Meals.DAILY_MEALS)
    departure_date = forms.ChoiceField(required=True,
                                        choices=User.DATES_2014)
    is_primary_driver = forms.BooleanField(label = "If you're parking on site: pick a primary driver/owner or renter of the vehicle.  Is it you? Yes? Then check here.", 
                                            required = True, 
                                            initial = False)
    has_car_on_site = forms.BooleanField(label ="Check here if you're driving or arriving in a vehicle to be parked in camp.")

    type_of_car = forms.ChoiceField(required=True, 
                                    choices = Travel.CAR_TYPES)
    make_of_vehicle = forms.CharField(label = _("What make if your car?"))

    width_of_vehicle = forms.CharField(label = _("How many feet wide is it?"))
    length_of_vehicle = forms.CharField(label = _("How long?"))
    car_color = forms.CharField(label = _("What color?"))
    lookingforride = forms.BooleanField(label= "Check here if you're looking for a ride either way.",
                                        required = False,
                                        initial = False)
    has_room_for_passenger_to_burn = forms.BooleanField(label = "Check here if you have room for another person on the way to the Playa.",
                                                required = False,
                                                initial = False)
    has_room_for_passenger_home = forms.BooleanField(label = "Check here if you have room for another person on the way home.",
                                                required = False,
                                                initial = False)
    needs_sherpa = forms.BooleanField(label = "Check here if you've got (a small amount of) cargo to send with others",
                                    required = False,
                                    initial = False)
    has_space = forms.BooleanField(label = "Check here if you can carry a bit of cargo for someone else",
                                    required = False,
                                    initial = False)    

    def clean_city(self):
        city = self.cleaned_data["from_city"]
        other = self.cleaned_data["other_place"]
        if city == "Other":
            raise ValidationError("Pleaes type in your city below")
            city = self.cleaned_data.get(other)
        else:
            city = self.cleaned_data.get(city)
        return self.cleaned_data  
    def clean_arrival(self):
        arrival = self.cleaned_data.get("arrival_date")
    def clean_first_meal(self):
        firstmeal = self.cleaned_data.get("first_meal")
    def clean_departure_date(self):
        departure = self.cleaned_data.get("departure_date")
    def can_take_passenger(self):
        has_space = self.cleaned_data.get("has_room_for_passenger")
    def looking_for_ride(self):
        seeks_ride = self.cleaned_data.get("lookingforride")
    def need_sherpa(self):
        need_sherpa = self.cleaned_data.get("has_space")


class MealSignups(forms.Form):
    def __init__(self, *args, **kwargs):
        super(MealSignups, self).__init__(*args, **kwargs)

        meals = Meal.objects.order_by('start_time')
        # FIXME: handle boolean courier
        positions = ['kp', 'sous']

        for meal in meals:
            for position in positions:
                field_name = self.field_name_for(meal, position)
                label = "%s: %s" % (meal.start_time.strftime("%d %m"), position)
                self.fields[field_name] = forms.BooleanField(label=label, required=False)

    def save(self, user, previous_signups):
        for field in self.fields:
            meal_id, position = self.meal_and_position_from(field)
            if self.cleaned_data[field]:
                MealSignup.objects.create(meal_id=meal_id, position=position, user=user)
            else:
                previous_signups.filter(meal_id=meal_id, position=position).delete()




    @staticmethod
    def field_name_for(meal, position):
        return "meal_%s_%s" % (meal.id, position)

    @staticmethod
    def meal_and_position_from(field_name):
        return field_name.split("_")[1:]



# if we didn't need dynamic meal days, something like that:
# class MealSignups(forms.Form):
#     kp_aug_20_am = forms.BooleanField(required=False)
#     sous_aug_20_am = forms.BooleanField(required=False)
#     chef_aug_20_am = forms.BooleanField(required=False)
#     courier_aug_20_am = forms.BooleanField(required=False)

#     kp_aug_20_pm = forms.BooleanField(required=False)
#     sous_aug_20_pm = forms.BooleanField(required=False)
#     chef_aug_20_pm = forms.BooleanField(required=False)
#     courier_aug_20_pm = forms.BooleanField(required=False)
    

class Meals(forms.Form):

   
    FIRST_OF_2014 = datetime.datetime(2014, 8, 20)
    setup1 = FIRST_OF_2014
    setup2 = FIRST_OF_2014 + datetime.timedelta(days=1)
    setup3 = FIRST_OF_2014 + datetime.timedelta(days=2)
    setup4 = FIRST_OF_2014 + datetime.timedelta(days=3)
    setup5 = FIRST_OF_2014 + datetime.timedelta(days=4)
    day1   = FIRST_OF_2014 + datetime.timedelta(days=5)
    day2   = FIRST_OF_2014 + datetime.timedelta(days=6)
    day3   = FIRST_OF_2014 + datetime.timedelta(days=7)
    day4   = FIRST_OF_2014 + datetime.timedelta(days=8)
    day5   = FIRST_OF_2014 + datetime.timedelta(days=9)
    day6   = FIRST_OF_2014 + datetime.timedelta(days=10)
    day7   = FIRST_OF_2014 + datetime.timedelta(days=11)
    day8   = FIRST_OF_2014 + datetime.timedelta(days=12)
    day9   = FIRST_OF_2014 + datetime.timedelta(days=13)


    date_choices = {setup1:FIRST_OF_2014,
    setup2:(FIRST_OF_2014 + datetime.timedelta(days=1)),
    setup3: (FIRST_OF_2014 + datetime.timedelta(days=2)),
    setup4: (FIRST_OF_2014 + datetime.timedelta(days=3)),
    setup5:(FIRST_OF_2014 + datetime.timedelta(days=4)),
    day1: (FIRST_OF_2014 + datetime.timedelta(days=5)),
    day2: (FIRST_OF_2014 + datetime.timedelta(days=6)),
    day3: (FIRST_OF_2014 + datetime.timedelta(days=7)),
    day4: (FIRST_OF_2014 + datetime.timedelta(days=8)),
    day5: (FIRST_OF_2014 + datetime.timedelta(days=9)),
    day6: (FIRST_OF_2014 + datetime.timedelta(days=10)),
    day7: (FIRST_OF_2014 + datetime.timedelta(days=11)),
    day8: (FIRST_OF_2014 + datetime.timedelta(days=12)),
    day9: (FIRST_OF_2014 + datetime.timedelta(days=13))}
     
    FIRST_OF_2014 = datetime.datetime(2014, 8, 20)
#    meals = []
#    meals.append()

    #meals = forms.CharField(required=True, choices = User_Meals.DAILY_MEALS)
    #shifts = forms.CharField(required=True, choices = User_Meals.SHIFTS)
    name = forms.CharField()
    # def clean_shifts(self):
    #     shifts = self.cleaned_data.get(choices = shifts)
    # def clean_meals(self):
    #     meals= self.cleaned_data.get(choices = meals)
    # def clean_name(self):
    #     name = self.cleaned_data.get(choices = name)
#below: melita's suggestion
    # def getForm(self):
    #     meal_shifts = [] 

    #     for i in range(26):
    #         meal_shifts = {
    #          'chef' : User_Meals.chef,
    #                 'sous_chef': User_Meals.sous_chef,
    #                 'kp': User_Meals.kp1}    




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
