from django.test import TestCase

class facebook_authentication_tests(TestCase):

	def test_login_flow(self):
		# using a valid facebook login flow a user can generate an access token to be stored

	def test_hostile_command(self):
		# if a command which is NOT from the dashboard is received by the facebook_data app it is rejected and reported to the account owner.



class facebook_post_interaction_tests(TestCase):

	def test_post_comment_command_from_dashboard(self):
		# when facebook_data app receives post_comment command from dashboard it successfully posts the comment in the right place

	def test_like_object_command_from_dashboard(self):
		# when facebook_data app receives like_comment command from dashboard it successfully likes the correct object

	def test_unlike_object_command_from_dashboard(self):
		# when facebook_data app receives unlike_comment command from dashboard it successfully unlikes the correct object



class facebook_CRUD_tests(TestCase):

	def test_previous_posts_command_from_dashboard(self):
		# when facebook_data_app receives previous_posts command it successfully receives AND feeds back the previous posts

	def test_new_post_command_from_dashboard(self):
		# when facebook_data app receives new_post command it successfully posts a new post

	def test_delete_object_command_from_dashboard(self):
		# when facebook_data app receives delete_object command it successfully deletes the new post


class facebook_statistics_test(TestCase):


# TODO - tests for failing gracefully

# Create your tests here.
