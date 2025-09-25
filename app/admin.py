from django.contrib import admin
from .models import *

class Eventadmin(admin.ModelAdmin):
    list_display=("id","username","email","password","location","time","date","image","created_at","phone")
    search_fields =("id","username")
    # list_filter=["description"]
    # readonly_fields=["time"]

# Register your models here.
admin.site.register(Event, Eventadmin)
