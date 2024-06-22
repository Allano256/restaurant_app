"""
URL configuration for restaurant_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from booking import views as booking_views
import debug_toolbar


urlpatterns = [
    path('admin/', admin.site.urls),
    path('booking/', include("booking.url"), name = 'booking' ),
    path("__debug__/", include("debug_toolbar.urls")),
    path('accounts/', include('allauth.urls')),
]

#Manage Admin titles
admin.site.site_header = "JO's Restaurant administration site."
admin.site.index_title = "Welcome to JO's Restaurant admin area..."