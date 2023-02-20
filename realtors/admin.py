from django.contrib import admin
from .models import Realtor

# Register your models here.

class RealtorAdmin(admin.ModelAdmin): #adds fields to list view of admin page   
    list_display = ("id", "name", "email", "hire_date")
    list_display_links = ("id", "name") #allow link
    search_fields = ("name",) #adds searchbox and define fields to text search from
    list_per_page = 25 # define max items per page


admin.site.register(Realtor, RealtorAdmin)    #adds fields to admin pages

