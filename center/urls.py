from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from center.views import index

urlpatterns = [
    path("home/", index, name='home'),
    path('admin/', admin.site.urls),
   
]