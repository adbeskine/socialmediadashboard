from django.conf.urls import url
from . import views

app_name = 'facebook_data'

urlpatterns = [
	url(r'^example_login/$', views.example_facebook_login, name='example_facebook_login'),
	url(r'^example_login_success/$', views.example_facebook_login_success, name='example_login_success')
]