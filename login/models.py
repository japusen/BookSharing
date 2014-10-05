from django.db import models
from django.contrib.auth.models import User

# class UserProfile(models.Model):
# 	user = models.OneToOneField(User)
# 	def __unicode__(self):
# 	    return "Umail: %s, Password: %s, Username: %s" % (self.user.email, self.user.password, self.user.username)
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    activation_key = models.CharField(max_length=40, blank=True)
    def __unicode__(self):
    	return "Umail: %s, Username: %s" % (self.user.email, self.user.username)

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
	uploader = models.CharField(max_length=20)
	date = models.DateField(auto_now_add=True)
	def __unicode__(self):
	    return "Course: %s, Title: %s, author: %s, edition: %s" % (self.course, self.title, self.author, self.edition)

class Recently_Submitted(models.Model):
	book = models.ForeignKey('Books')
	date = models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
	    return "Course: %s, Course title: %s, Book title: %s" % (self.book.course.courseCode, self.book.course.courseTitle, self.book.title)