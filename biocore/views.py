from django.shortcuts import render, redirect, render_to_response

from django.http import HttpResponse

from django.contrib import auth
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import AuthenticationForm

from django.core.urlresolvers import reverse

from biocore import forms  
from biocore.models import MealSignup

from django.views.generic import ListView

from models import User
from datetime import datetime
import datetime
from django.template.loader import get_template
from django.template import Context, loader, RequestContext


def hello(request):
	return HttpResponse("Hello world")

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
#
#def hours_ahead(request, offset):
#	try:
#		offset = int(offset)
#	except ValueError:
#		raise Http404()
#	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
#	html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
#	return HttpResponse(html)

def hours_ahead(request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	# t = get_template('hours_ahead.html')
	#html = t.render(Context({'future': dt}))
	return render(request, 'hour_ahead.html', {'hour_offset': offset,'future':dt})

def daystoburn(request):
	next_burn = datetime.datetime(2014, 8, 30)
	now = datetime.datetime.now()
	days_until_burn = (next_burn - now).days
	#html = "<html><body>The Man burns in %s days.</body></html>" %days_until_burn
	#t = get_template('daysuntilburn.html')
	#html = t.render(Context({'daystoburn': days_until_burn}))
	return render(request, 'daysuntilburn.html', {'daystoburn': days_until_burn})

class ListUserView(ListView):
	model = User

def _redirect_if_logged_in(f):
	from functools import wraps
	wraps(f)
	def _f(request, *args, **kwargs):
		next = request.GET.get("next", reverse('homepage'))
		if request.user.is_authenticated():
			return redirect(next)
		return f(request, *args, **kwargs)
	return _f


# example longform equivalent of shortcuts.render:
# from django.template.loader import get_template
# from django.template.context import RequestContext
# from django.http import HttpResponse
#
# partial_context = { 'data': 'from view' }
# context = RequestContext(request, partial_context)
# template = get_template('homepage.html')
# result = template.render(context)
# response = HttpResponse(result)
# return response
# -or- w/ shortcuts.render:
# 
# return render(request, 'homepage.html', partial_context)

def homepage(request):
	return render(request, 'homepage.html')

def profile(request, user_id):
	return HttpResponse("TBD")

@_redirect_if_logged_in
def login(request):
	login_form = AuthenticationForm()
	if request.method == 'POST':
		# django takes form names and filling in field names as keys in the .POST MultiValueDict
		# something like: request.POST = {'username': 'foo'}
		login_form = AuthenticationForm(request, request.POST)

		if login_form.is_valid():
			user = login_form.get_user()

			if user is not None:
				auth.login(request, user)

				next = request.GET.get("next", reverse('homepage'))
				return redirect(next)

	request.session.set_test_cookie()
	return render(request, 'login.html', {
		'login_form': login_form
	})
	#if the 

def logout(request):
	next = request.GET.get("next", reverse('homepage'))
	auth.logout(request)
	return redirect(next)

@_redirect_if_logged_in
def register(request):
	registration_form = forms.UserCreationForm()
	if request.method == 'POST':
		registration_form = forms.UserCreationForm(request.POST)

		if registration_form.is_valid():
			user = registration_form.save()
			user.backend = 'django.contrib.auth.backends.ModelBackend'
			auth.login(request, user)
			return redirect(reverse('homepage'))

	return render(request, 'register.html', {
		'registration_form': registration_form
	})

@login_required
def travel(request):
	travel_from = forms.TravelFrom()
	if request.method == "POST":
		travel_from = forms.TravelFrom(request.POST)

	return render(request, 'travel.html', {
		'travel_from': travel_from
	})

# date_choices = User.DATES_2014



@login_required
def meal_signup(request):
	existing_signups = MealSignup.objects.filter(user=request.user)
	initial = {}
	for signup in existing_signups:
		field_name = forms.MealSignups.field_name_for(signup.meal, signup.position)
		initial[field_name] = True

	# initial should include previous signups.
	#initial = User_Meals.objects.filter(user=request.user)
	# e.g. initial = {'sous_aug_20_am': True}
	#  to match the form field

	form = forms.MealSignups(initial=initial)
	if request.method == 'POST':
		form = forms.MealSignups(request.POST, initial=initial)
		if form.is_valid():
			form.save(request.user, existing_signups)


	return render(request, 'meal_signup.html', {'form': form})


# def meals(request):
# 	date_choices = User.DATES_2014 
# 	meals1 = forms.Meals()
	#display all dates
	# if request.method == "POST":
	# 	meals = forms.Meals(request.POST)
	# if request.method == "GET":
	# #just render the form
	# # get form from forms
	# # form = forms.Meals().getForm()
	# #below listed dates successfully.
	# 	return render_to_response('meals.html', {'date_choices': date_choices})
	# #else:
	# #old method below. 
	# if request.method == "POST":
	# 	form = Meals(request.POST)
	# 	if form.is_valid():
	# 		shifts = form.cleaned_data['shifts']
	# 		meals = form.cleaned_data['meals']
	# 		dates = form.cleaned_data['']


	# 		model_instance.save()
	# 		return redirect('your data has been saved')
	# return render(request 'meals.html', {'form': form,
	# 	})


# #class based view 
# class MyView(View):

# 	def get(self, request, *args, **kwargs):
# 		return HttpResponse("Hello, World")

# #for listing contacts
# class ListContactView(ListView):
# 	model = Contact 
# 	template_name = 'contact_list.html'

# #adding info to database
# class CreateContactView(CreateView):

# 	model = Contact
# 	template_name = 'edit_contact.html'
# 	#tells view to use extra field in forms.py
# 	form_class = forms.ContactForm

# 	def get_success_url(self):
# 		return reverse('contacts-list')
# #information about where the formshould redirect to the context

# 	def get_context_data(self, **kwargs):

# 		context = super(CreateContactView, self).get_context_data(**kwargs)
# 		context['action'] = reverse('contacts-new')

# 		return context

# class ContactListViewTest(TestCase):

# 	def test_contacts_in_the_context(self):

# 		client = Client()
# 		response = client.get('/')

# 		self.assertEquals(list(response.context['object_list']), [])

# 		Contact.objects.create(first_name='foo', last_name='bar')
# 		response = client.get('/')
# 		self.assertEquals(response.context['object_list'].count(), 1)

# 	def test_contacts_in_the_context_request_factory(self):

# 		factory = RequestFactory()
# 		request = factory.get('/')

# 		response = ListContactView.as_view()(request)

# 		self.assertEquals(list(response.context_data['object_list']), [])

# 		Contact.objects.create(first_name = 'foo', last_name='bar')
# 		response = ListContactView.as_view()(request)
# 		self.assertEquals(response.context_data['object_list'].count(), 1)

# class ContactListIntegrationTests(LiveServerTestCase):

# 	@classmethod
# 	def setUpClass(cls):
# 		cls.selenium = WebDriver()
# 		super(ContactListIntegrationTests, cls).setUpClass()

# 	@classmethod
# 	def tearDownClass(cls):
# 		cls.selenium.quit()
# 		super(ContactListIntegrationTests, cls).tearDownClass()

# 	def test_contact_listed(self):
# 		#create test contact
# 		Contact.objects.create(first_name='foo', last_name='bar')
# 		#make sure it's listed as <first><last> on the list
# 		self.selenium.get('%s%s' %(self.live_server_url, '/'))
# 		self.assertEqual(
# 			self.selenium.find_elements_by_css_selector('contact')['0'].text, 'foo.bar'
# 			)
# 	def test_add_contact(self):


# 		self.selenium.find_element_by_link_text('add contact').click()

# 		self.selenium.find_element_by_id('id_first_name').send_keys('test')
# 		self.selenium.find_element_by_id('id_last_name').send_keys('contact')
# 		self.selenium.find_element_by_id('id_email').send_keys('test@example.com')

# 		self.selenium.find_element_by_id("save_contact").click()
# 		self.assertEqual(
# 		self.selenium.find_elements_by_css_selector('.contact')[-1].text,'test contact'
# 		)

# #allows us to edit contacts
# class UpdateContactView(UpdateView):
# 	model = Contact
# 	template_name = 'edit_contact.html'
# 	#references forms.py
# 	form_class = forms.ContactForm

# 	def get_success_url(self):
# 		return reverse('contacts-list')

# 	def get_context_data(self, **kwargs):

# 		context = super(UpdateContactView, self).get_context_data(**kwargs)
# 		context['action'] = reverse('contacts-edit',
# 			kwargs= {'pk': self.get_object().id})

# 		return context

# class DeleteContactView(DeleteView):

#     model = Contact
#     template_name = 'delete_contact.html'

#     def get_success_url(self):
#         return reverse('contacts-list')


# class ContactView(DetailView):

# 	model = Contact
# 	template_name = 'contact.html'

# class Contact(models.Model):

# 	def get_absolute_url(self):

# 		return reverse("contacts-view", kwargs={'pk':self.id})

# class EditContactAddressView(UpdateView):

# 	model = Contact
# 	template_name = 'edit_addresses.html'
# 	form_class = forms.ContactAddressFormSet

# 	def get_success_url(self):
# 		# redirect to the Contact view.
# 		return self.get_object().get_absolute_url()

