from django.conf.urls import patterns, include, url

#allows for url mapping of contact list view
import contacts.views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()


urlpatterns = patterns('',
	#url function lets  you use named parameters to make everything more clear. 
	#the regex w trailing dollar sign matches end of the line. 
	url(r'^$', contacts.views.ListContactView.as_view(),
		name = 'contacts-list',),
	url(r'^new$', contacts.views.CreateContactView.as_view(),
		name='contacts-new',),
	
    # Examples:
    # url(r'^$', 'addressbook.views.home', name='home'),
    # url(r'^addressbook/', include('addressbook.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
