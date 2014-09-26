from django.contrib import admin
from login.models import UserInfo, Department, Course, Books, Recently_Submitted

# Register your models here.
class UserAdmin(admin.ModelAdmin):
	list_display = ('umail', 'password', 'username')
	search_fields = ['umail', 'username']

class DeptAdmin(admin.ModelAdmin):
	list_display = ('dept', 'deptName')
	search_fields = ['deptName']

class CourseAdmin(admin.ModelAdmin):
	list_display = ('dept', 'courseCode', 'courseNo', 'courseLetter', 'courseTitle')
	search_fields = ['courseCode']

class BookAdmin(admin.ModelAdmin):
	list_display = ('course', 'title')
	search_fields = ['course', 'title']

class RecentSubAdmin(admin.ModelAdmin):
	list_display = ('courseCode', 'title', 'date')
	search_fields = ('courseCode', 'title', 'date')

admin.site.register(UserInfo, UserAdmin)
admin.site.register(Department, DeptAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Books, BookAdmin)
admin.site.register(Recently_Submitted, RecentSubAdmin)