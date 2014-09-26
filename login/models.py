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
	def __unicode__(self):
	    return "Department: %s, Name: %s\n" % (self.dept, self.deptName)

class Course(models.Model):
	dept = models.ForeignKey('Department')
	courseCode = models.CharField(max_length=15, primary_key=True)
	courseTitle = models.CharField(max_length=100)
	courseNo = models.IntegerField()
	courseLetter = models.CharField(max_length=10, blank=True)
	def __unicode__(self):
	    return "Course: %s, Dept: %s, Title: %s" % (self.courseCode, self.dept, self.courseTitle)

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
	def __unicode__(self):
	    return "Course: %s, Title: %s, author: %s, edition: %s" % (self.course, self.title, self.author, self.edition)

class Recently_Submitted(models.Model):
	courseCode = models.CharField(max_length=15)
	courseTitle = models.CharField(max_length=50)
	title = models.CharField(max_length=100)
	date = models.DateTimeField()
	def __unicode__(self):
	    return "Course: %s, Course title: %s, Book title: %s" % (self.courseCode, self.courseTitle, self.title)