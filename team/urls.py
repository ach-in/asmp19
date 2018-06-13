from django.conf.urls import url
from . import views
#your url for the registration app
app_name='team'

urlpatterns =[
	url(r'^$', views.team, name='team'),
]