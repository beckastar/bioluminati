from django.conf.urls import patterns, include, url 

#allows for url mapping of contact list view

#includes staticfiles
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from biocore import views
from biocore.views import hello, current_datetime, daystoburn, hours_ahead
from django.contrib import admin
admin.autodiscover()
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover() 



urlpatterns = patterns('',
    url(r'^$', views.homepage, name='homepage'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^register/$', views.register, name='register'),
    # example regex-based urlconf, e.g. 
    # /profiles/2/ -> views.profile(user_id=2)
    url(r'^profiles/(?P<user_id>\d+)/$', views.profile, name='profile'),
    #2 lines of tutorial below
    url(r'^hello/$', hello),
    url(r'^time/$', current_datetime),
    #below line needs front end
    url(r'^days/$', daystoburn),
    #tutorial below
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    (r'^travel/$', views.travel),
    url(r'^meal_signup/$', views.meal_signup, name='meal_signup'),
    url(r'^chef_cockpit/(?P<meal_id>\d+)/$', views.chef_cockpit, name='chef_cockpit'),
    (r'^admin/', include(admin.site.urls)),

    #url(r'^$', views.ListContactView.as_view(),
    #    name = 'contacts-list',),
	#url function lets  you use named parameters to make everything more clear. 
	#the regex w trailing dollar sign matches end of the line. 
	# url(r'^$', views.ListContactView.as_view(),
	# 	name = 'contacts-list',),
	# url(r'^new$', views.CreateContactView.as_view(),
	# 	name='contacts-new',),
	# url(r'^edit/(?P<pk>\d+)/$', views.UpdateContactView.as_view(),
	# 	name='contacts-edit',),
	# url(r'^delete/(?P<pk>\d+)/$', views.DeleteContactView.as_view(),
 #        name='contacts-delete',),
	# url(r'^(?P<pk>\d+)/$', views.ContactView.as_view(),
	# 	name='contacts-view',),
	# url(r'^edit/(?P<pk>\d+)/addresses$', views.EditContactAddressView.as_view(),
 #        name='contacts-edit-addresses',),
	
    # Examples:
    # url(r'^$', 'addressbook.views.home', name='home'),
    # url(r'^addressbook/', include('addressbook.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()