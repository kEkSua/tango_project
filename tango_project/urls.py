"""tango_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rango import views
from registration.backends.simple.views import RegistrationView


class MyRegistrationView(RegistrationView):
    success_url = 'rango:register_profile'

urlpatterns = [
    path('', views.index, name='index'),
    path('rango/', include('rango.urls')),
    path('admin/', admin.site.urls),
    path('accounts/register/', MyRegistrationView.as_view(), name='registration_register'),
    path('accounts/', include('registration.backends.simple.urls')),
    path('search/', views.search, name='search')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


