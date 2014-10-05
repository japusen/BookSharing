from django.contrib import admin
from login.models import Department, Course, Books, Recently_Submitted
from django.contrib.auth.models import User

# Register your models here.
class DeptAdmin(admin.ModelAdmin):
	list_display = ('dept', 'deptName')
	search_fields = ['deptName']

class CourseAdmin(admin.ModelAdmin):
	list_display = ('dept', 'courseCode', 'courseNo', 'courseLetter', 'courseTitle')
	search_fields = ['courseCode']

class BookAdmin(admin.ModelAdmin):
	list_display = ('course', 'title', 'date')
	search_fields = ['course', 'title']

class RecentSubAdmin(admin.ModelAdmin):
	list_display = ('book', 'date')
	search_fields = ('book', 'date')

admin.site.register(Department, DeptAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Books, BookAdmin)
admin.site.register(Recently_Submitted, RecentSubAdmin)