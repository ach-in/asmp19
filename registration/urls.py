from django.conf.urls import url
from . import views
#your url for the registration app

app_name='registration'

urlpatterns = [
	url(r'^$', views.registration, name='registration'),
	url(r'^mentorlist$', views.mentor_list, name='mentor_list'),
	url(r'^mentorlist/finance/$',views.finance, name='finance'),
	url(r'^mentorlist/management/$',views.management, name='management'),
	url(r'^mentorlist/analytics/$',views.analytics, name='analytics'),
	url(r'^mentorlist/manageconsult/$', views.manageconsult, name='manageconsult'),
	url(r'^mentorlist/strategyconsult/$', views.strategyconsult, name='strategyconsult'),
	url(r'^mentorlist/core/$', views.core, name='core'),
	url(r'^mentorlist/research/$', views.research, name='research'),
	url(r'^mentorlist/designno/$', views.designno, name='designno'),
	url(r'^mentorlist/civilservice/$', views.civilservice, name='civilservice'),
	url(r'^mentorlist/it/$', views.infotech, name='infotech'),
	url(r'^mentorlist/(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.mentor_detail, name='mentor_detail'),
]
