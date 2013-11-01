from django.conf.urls import patterns, include, url 

#allows for url mapping of contact list view

#includes staticfiles
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
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
	url(r'^edit/(?P<pk>\d+)/$', contacts.views.UpdateContactView.as_view(),
		name='contacts-edit',),
	url(r'^delete/(?P<pk>\d+)/$', contacts.views.DeleteContactView.as_view(),
        name='contacts-delete',),
	url(r'^(?P<pk>\d+)/$', contacts.views.ContactView.as_view(),
		name='contacts-view',),
	url(r'^edit/(?P<pk>\d+)/addresses$', contacts.views.EditContactAddressView.as_view(),
        name='contacts-edit-addresses',),
	
    # Examples:
    # url(r'^$', 'addressbook.views.home', name='home'),
    # url(r'^addressbook/', include('addressbook.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()