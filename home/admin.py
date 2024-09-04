from django.contrib import admin

from .models import Amenities, Hotel, Hotelimages, HotelBooking

# Register your models here.
admin.site.register(Amenities)
admin.site.register(Hotel)
admin.site.register(Hotelimages)
admin.site.register(HotelBooking)
