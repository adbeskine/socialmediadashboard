from django.conf.urls import url
from . import views

app_name = 'render_dashboard'

urlpatterns = [
	url(r'^$', views.dashboard, name='dashboard')
]