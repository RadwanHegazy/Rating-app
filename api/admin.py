from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Product, Star



class ProductPanel (admin.ModelAdmin) : 
    list_display = ['title','averge_starts','price']
    search_fields = ['title']

class StarsPanel (admin.ModelAdmin) : 
    list_display = ['user','product','star']
    list_filter = ['product']

# add in admin panel
admin.site.register(Product, ProductPanel)
admin.site.register(Star, StarsPanel)


# remove from admin panel
admin.site.unregister(Group)