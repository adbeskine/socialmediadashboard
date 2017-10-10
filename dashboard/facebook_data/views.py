from django.shortcuts import render
import requests


def example_facebook_login(request):
	return render(request, 'facebook_data/login_example.html')

# Create your views here.
def example_facebook_login_success(request):
	code = request.GET.get('code', None)
	at = requests.get('https://graph.facebook.com/v2.10/oauth/access_token?client_id=121844948527784&redirect_uri=https://www.facebook.com/v2.10/dialog/oauth?client_id=121844948527784&redirect_uri=https://97dd129e.ngrok.io/facebook_data/example_login_success/&scope=manage_pages&client_secret=3d6d56f8ab4ed5be989afcab64fb6228&code={}'.format(code)).json()
	access_token = at['access_token']
	r = requests.get('https://graph.facebook.com/me/accounts?access_token={}'.format(access_token))
	accounts = r.json()
	context = {'raw_text':accounts}
	return render(request, 'facebook_data/example_login_success.html', context)
