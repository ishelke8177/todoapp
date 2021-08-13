from django.contrib import admin
from .models import Task

# Register your models here.

admin.site.site_header = 'TodoAdmin'
admin.site.index_title  =  "Admin"

# register models
# note user model is already registerd
admin.site.register(Task)