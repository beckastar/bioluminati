# Create your views here.
from django.http import HttpResponse
from django.views.generic import View
#for listing contacts
from django.views.generic import ListView
from contacts.models import Contact
#adding info to database
from django.core.urlresolvers import reverse
from django.views.generic import CreateView


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
