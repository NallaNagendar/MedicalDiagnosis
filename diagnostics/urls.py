"""
URL configuration for diagnostics project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from . import views
from doctor import views as d_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', d_views.home1,name='home1'),
    path('admin/', admin.site.urls),
    path('doctor/', include('doctor.urls')),  # Include doctor app URLs
    path('patient/', include('patient.urls')),  # Include patient app URLs
    path('appointments/', include('appointments.urls')),  # Include appointments app URLs
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
