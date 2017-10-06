from django.test import TestCase

class dashboard_config_options(TestCase):

	def test_add_facebook_stream(self):
		# a user can successfully autheticate with facebook, connect to a page and have the page data begin rendering on the dashboard


class dashboard_commands_facebook(TestCase):

	def test_fetch_feed(self):
		# when a stream is loaded it correctly fetches the feed of the page it's linked to

	def test_new_post(self):
		# when a new_post command is sent from the dashboard a new post is posted, the page refreshes and the new post appears correctly

	def test_delete_object(self):
		# when a delete_object command is sent from the dashboard the object is deleted from facebook.
		# note: the delete object option will not be available to a user on an object he does not have permission to delete

	def test_post_comment(self):
		# when a post_comment command is sent from the dashboard the comment is posted, the dashboard refreshes and the comment appears correctly

	def test_like_object(self):
		# when a like_object command is sent from the dashboard the object is liked, the dashboard refreshes and the like appears correctly

	def test_unlike_object(self):
		# when an unlike_object command is sent from the dashboard the object is unliked, the dashboard refreshes and the object correctly appears unliked

# TODO - tests for failing gracefully


# Create your tests here.
