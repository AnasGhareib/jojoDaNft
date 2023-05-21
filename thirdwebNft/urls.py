from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.landingPage, name="landingPage"),
    path("listingNFT/", views.listingNFT, name="listingNFT"),
    path("showroom/", views.showroom, name="showroom"),
    path("success", views.success, name="success"),
   
]