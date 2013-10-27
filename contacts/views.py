# Create your views here.
from django.http import HttpResponse
from django.views.generic import View
#for listing contacts
from django.views.generic import ListView
from contacts.models import Contact
#adding info to database
from django.core.urlresolvers import reverse
from django.views.generic import CreateView
#testing
from django.test.client import Client 
from django.test.client import RequestFactory
from django.test import LiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver  
#missing from tutorial; this broke the whole thing
from unittest import TestCase
from django.views.generic import UpdateView
#for deleting contacts
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.db import models 
import forms 

#general view 
def hello_world(request):
	return HttpResponse("Hello, World")

#class based view 
class MyView(View):

	def get(self, request, *args, **kwargs):
		return HttpResponse("Hello, World")

#for listing contacts
class ListContactView(ListView):
	model = Contact 
	template_name = 'contact_list.html'

#adding info to database
class CreateContactView(CreateView):

	model = Contact
	template_name = 'edit_contact.html'
	#tells view to use extra field in forms.py
	form_class = forms.ContactForm

	def get_success_url(self):
		return reverse('contacts-list')
#information about where the formshould redirect to the context

	def get_context_data(self, **kwargs):

		context = super(CreateContactView, self).get_context_data(**kwargs)
		context['action'] = reverse('contacts-new')

		return context

class ContactListViewTest(TestCase):

	def test_contacts_in_the_context(self):

		client = Client()
		response = client.get('/')

		self.assertEquals(list(response.context['object_list']), [])

		Contact.objects.create(first_name='foo', last_name='bar')
		response = client.get('/')
		self.assertEquals(response.context['object_list'].count(), 1)

	def test_contacts_in_the_context_request_factory(self):

		factory = RequestFactory()
		request = factory.get('/')

		response = ListContactView.as_view()(request)

		self.assertEquals(list(response.context_data['object_list']), [])

		Contact.objects.create(first_name = 'foo', last_name='bar')
		response = ListContactView.as_view()(request)
		self.assertEquals(response.context_data['object_list'].count(), 1)

class ContactListIntegrationTests(LiveServerTestCase):

	@classmethod
	def setUpClass(cls):
		cls.selenium = WebDriver()
		super(ContactListIntegrationTests, cls).setUpClass()

	@classmethod
	def tearDownClass(cls):
		cls.selenium.quit()
		super(ContactListIntegrationTests, cls).tearDownClass()

	def test_contact_listed(self):
		#create test contact
		Contact.objects.create(first_name='foo', last_name='bar')
		#make sure it's listed as <first><last> on the list
		self.selenium.get('%s%s' %(self.live_server_url, '/'))
		self.assertEqual(
			self.selenium.find_elements_by_css_selector('contact')['0'].text, 'foo.bar'
			)
	def test_add_contact(self):


		self.selenium.find_element_by_link_text('add contact').click()

		self.selenium.find_element_by_id('id_first_name').send_keys('test')
		self.selenium.find_element_by_id('id_last_name').send_keys('contact')
		self.selenium.find_element_by_id('id_email').send_keys('test@example.com')

		self.selenium.find_element_by_id("save_contact").click()
		self.assertEqual(
		self.selenium.find_elements_by_css_selector('.contact')[-1].text,'test contact'
		)

#allows us to edit contacts
class UpdateContactView(UpdateView):
	model = Contact
	template_name = 'edit_contact.html'
	#references forms.py
	form_class = forms.ContactForm

	def get_success_url(self):
		return reverse('contacts-list')

	def get_context_data(self, **kwargs):

		context = super(UpdateContactView, self).get_context_data(**kwargs)
		context['action'] = reverse('contacts-edit',
			kwargs= {'pk': self.get_object().id})

		return context

class DeleteContactView(DeleteView):

    model = Contact
    template_name = 'delete_contact.html'

    def get_success_url(self):
        return reverse('contacts-list')


class ContactView(DetailView):

	model = Contact
	template_name = 'contact.html'

class Contact(models.Model):

	def get_absolute_url(self):

		return reverse("contacts-view", kwargs={'pk':self.id})
