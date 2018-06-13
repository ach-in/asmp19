from django.conf.urls import url
from . import views
#your url for the registration app
app_name='home'

urlpatterns =[
	url(r'^$', views.home, name='home'),
]