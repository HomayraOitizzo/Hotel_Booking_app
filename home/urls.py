from django.contrib import admin
from django.urls import path
from  .views import * 
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .models import Amenities, Hotel

urlpatterns = [
   path('', home, name='home'),
    path('login/', login_page, name='login_page'),
     path('register/', register_page, name='register_page'),
     path('hotel-detail/<uid>', hotel_detail, name='hotel_detail')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()