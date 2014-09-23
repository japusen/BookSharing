from django.db import models

class UserInfo(models.Model):
	umail = models.EmailField(primary_key=True)
	password = models.CharField(max_length=15)
	username = models.CharField(max_length=15, unique=True)
	def __unicode__(self):
	    return "Umail: %s, Password: %s, Username: %s" % (self.umail, self.password, self.username)


class Department(models.Model):
	dept = models.CharField(max_length=10, primary_key=True)
	deptName = models.CharField(max_length=50)

class Course(models.Model):
	courseCode = models.CharField(max_length=15, primary_key=True)
	dept = models.ForeignKey('Department')
	courseTitle = models.CharField(max_length=50)

class Books(models.Model):
	course = models.ForeignKey('Course')
	title = models.CharField(max_length=100)
	author = models.CharField(max_length=50)
	edition = models.IntegerField()
	dLink = models.URLField()
	file_type_choices = (
		('pdf', 'pdf'),
		('epub', 'epub'),
		('djvu', 'djvu'),
		('torrent', 'torrent'),
		('other', 'other')
	)
	fileType = models.CharField(max_length=10, choices=file_type_choices)
	upvotes = models.IntegerField()
	downvotes = models.IntegerField()

class Recently_Submitted(models.Model):
	courseCode = models.CharField(max_length=15, primary_key=True)
	courseTitle = models.CharField(max_length=50)
	title = models.CharField(max_length=100)
	date = models.DateTimeField()