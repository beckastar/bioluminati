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

	def get_success_url(self):
		return reverse('contacts-list')

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


