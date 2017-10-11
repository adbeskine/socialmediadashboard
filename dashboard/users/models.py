from django.db import models

class Dashboard_user(models.Model):
	username = models.CharField(max_length=30)
	password = models.CharField(max_length=30)
	email = models.CharField(max_length=30)

	def __str__(self):
		return "%s %s" % (self.username, self.email)

class Stream(models.Model):
	service = models.CharField(max_length=30) # fb/tw/Li/ig
	name = models.CharField(max_length=30)
	fb_id = models.CharField(max_length=30, default="N.A") # page_id
	fb_access_token = models.CharField(max_length=30, default="N.A")
	user = models.ForeignKey(Dashboard_user, on_delete = models.CASCADE)

	def __str__(self):
		return "%s %s %s" % (self.service, self.name)

# Create your models here.
