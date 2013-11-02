from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

class ForceEssentialAnswersMiddleware(object):
	def __init__(self):
		self.essential_answer_pages = (reverse('homepage'),)
	def process_request(self, request):
		if not request.user.is_authenticated():
			return None
		if request.user.has_answered_essentials():
			return None
		if request.path not in self.essential_answer_pages:
			return HttpResponseRedirect(reverse('homepage'))

# decide what data is essential for people to answer.
# build the list of pages that allow people to answer that. - add that to the list of essential_answer_pages.
# only force people who are: logged in, have not answered everything, and are not visiting one of the essential pages.
