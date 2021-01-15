from django.contrib import admin
from .models import PriceIndex

class PriceIndexAdmin(admin.ModelAdmin):
    list_display = ('name','price')  
    empty_value_display = '-empty-'    
    list_filter = ('name', 'price')    
    list_per_page = 25                  
    ordering = ['-price', 'name']    

# and register it 
admin.site.register(PriceIndex, PriceIndexAdmin)