from django.contrib import admin

# Register your models here.
import csv
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from django.contrib import admin
from .models import Department, Class, Course, UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    actions = ['upload_users']

    def upload_users(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="user_upload_template.csv"'

        writer = csv.writer(response)
        writer.writerow(['id', 'name', 'phone_no', 'email', 'department_id', 'class_id', 'course_ids'])

        return response

    upload_users.short_description = "Upload Users CSV Template"

admin.site.register(UserProfile, UserProfileAdmin)
