from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Dashboard_user
from .forms import RegisterForm

def login(request):
	if request.method == 'POST':
		pass # check login details etc etc
	return render(request, 'users/login.html', {'RegisterForm':RegisterForm})

def register(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']#TODO hash passwords
			email = form.cleaned_data['email']
			new_user = Dashboard_user(username=username, password=password, email=email)
			new_user.save()
	return redirect(reverse('users:login'))
# Create your views here.
