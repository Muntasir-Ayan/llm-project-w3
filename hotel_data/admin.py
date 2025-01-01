from django.contrib import admin
from .models import Hotel, GeneratedTitleDesc, SummaryTable

class HotelAdmin(admin.ModelAdmin):
    list_display = ('hotel_id', 'city_name', 'title', 'price', 'rating', 'room_type', 'location')
    search_fields = ('title', 'city_name', 'hotel_id')
    list_filter = ('city_name', 'room_type', 'rating')

class GeneratedTitleDescAdmin(admin.ModelAdmin):
    list_display = ('hotel_id', 'title', 'generated_title')
    search_fields = ('hotel_id', 'generated_title')
    list_filter = ('hotel_id',)

class SummaryTableAdmin(admin.ModelAdmin):
    list_display = ('hotel_id', 'rating', 'review')
    search_fields = ('hotel_id', 'review')
    list_filter = ('rating',)

# Register models with custom admin options
admin.site.register(Hotel, HotelAdmin)
admin.site.register(GeneratedTitleDesc, GeneratedTitleDescAdmin)
admin.site.register(SummaryTable, SummaryTableAdmin)
