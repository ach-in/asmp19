from django.conf.urls import url
from . import views
#your url for the registration app

app_name='registration'

urlpatterns =[
	url(r'^$', views.registration, name='registration'),
	url(r'^mentorlist/$', views.mentor_list, name='mentor_list'),
	url(r'^mentorlist/finance/$',views.finance, name='finance'),
	url(r'^mentorlist/analytics/$',views.analytics, name='analytics'),
	url(r'^mentorlist/consult/$', views.consult, name='consult'),
	url(r'^mentorlist/management/$', views.consult, name='management'),
	url(r'^mentorlist/research/$', views.consult, name='research'),
	url(r'^mentorlist/consult/$', views.consult, name='consult'),
	url(r'^mentorlist/(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.mentor_detail, name='mentor_detail'),
]
