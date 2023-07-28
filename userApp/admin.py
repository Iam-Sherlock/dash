from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from userApp.models import CourseSelection

class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name','password']
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
@admin.register(CourseSelection)
class CourseSelectionAdmin(admin.ModelAdmin):
    pass