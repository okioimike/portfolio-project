from django.contrib import admin
from .models import Job

#admin.site.register(Job)
@admin.register(Job)
class jobAdmin(admin.ModelAdmin):
    list_display = ['image', 'summary']
