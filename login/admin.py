from django.contrib import admin
from login.models import UserInfo

# Register your models here.
class UserAdmin(admin.ModelAdmin):
	list_display = ('umail', 'password', 'username')
	search_fields = ['umail', 'username']

admin.site.register(UserInfo, UserAdmin)