from django.shortcuts import render
import requests

####################################
#########PROTOTYPE##################
####################################


def example_facebook_login(request):
	return render(request, 'facebook_data/login_example.html')

# Create your views here.
def example_facebook_login_success(request):
	code = request.GET.get('code', None) #1. get the first code from the initialization of the login flow
	#2. client_id -> redirect_uri(the exact url which initialized the login flow) -> client-secret -> code from step 1 | this swaps the code for a proper access token used in graph API calls
	at = requests.get('https://graph.facebook.com/v2.10/oauth/access_token?client_id=121844948527784&redirect_uri=https://www.facebook.com/v2.10/dialog/oauth?client_id=121844948527784&redirect_uri=https://97dd129e.ngrok.io/facebook_data/example_login_success/&scope=manage_pages&client_secret=3d6d56f8ab4ed5be989afcab64fb6228&code={}'.format(code)).json()
	access_token = at['access_token'] #3. returns the access token
	aat = requests.get('https://graph.facebook.com/v2.10/oauth/access_token?client_id=121844948527784&client_secret=3d6d56f8ab4ed5be989afcab64fb6228&grant_type=client_credentials').json()#4. generate app access token (to inspect access token)
	app_access_token = aat['access_token']
	it = requests.get('https://graph.facebook.com/debug_token?input_token={}&access_token={}'.format(access_token, app_access_token)).json() #5. inspect the user access token using app access token
	if it['data']['is_valid'] == True:
		pass
	else:
		return render(request, 'error, security keys failed verification') #5. if the user access token doesn't verify abort
	raw_accounts = requests.get('https://graph.facebook.com/me/accounts?access_token={}'.format(access_token)).json() #6. get all user pages
	accounts = raw_accounts['data']
	context = {'accounts':accounts}
	return render(request, 'facebook_data/example_login_success.html', context)


def example_facebook_stream(request, page_id, access_token): # in the returned json from a successful login, access_token = entry.access_token (see above), id=entry.id(see above)
	f = requests.get('https://graph.facebook.com/{page_id}/feed?access_token={access_token}'.format(page_id=page_id, access_token=access_token))
	stream = f.json()['data']
	context = {'stream':stream}
	return render(request, 'facebook_data/example_stream.html', context)


#########################################################################################

