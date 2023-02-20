from django.contrib import admin
from .models import Listing

# Register your models here.
class ListingAdmin(admin.ModelAdmin): #adds fields to list view of admin page   
    list_display = ("id", "title", "is_published", "price", "list_date", "realtor")
    list_display_links = ("id", "title") #allow link
    list_filter  = ("realtor","is_published") #adds filter
    list_editable = ("is_published", ) #allow direct edit on list page
    search_fields = ("title", "description", "address", "city", "state", "zipcode", "price") #adds searchbox and define fields to text search from
    list_per_page = 4 # define max items per page

admin.site.register(Listing, ListingAdmin)    #adds fields to admin pages. First parameter adds model to admin top. Second adds fields to admin top > model top page.
