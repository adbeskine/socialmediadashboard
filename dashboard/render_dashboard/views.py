from django.shortcuts import render


def dashboard(request):
	return render(request, 'render_dashboard/dashboard.html')
# Create your views here.
