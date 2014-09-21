from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserInfo(models.Model):
	umail = models.EmailField(primary_key=True)
	password = models.CharField(max_length=15)
	username = models.CharField(max_length=15, unique=True)
	def __unicode__(self):
	    return "Umail: %s, Password: %s, Username: %s" % (self.umail, self.password, self.username)