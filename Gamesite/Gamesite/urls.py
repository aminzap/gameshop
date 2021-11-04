"""Gamesite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib.auth import views as authenticate
from django.urls import path, include

from user import views as user_view


urlpatterns = [
                  path("admin/", admin.site.urls),
                  path('game/', include('game.urls')),
                  path('sign-up/', user_view.register, name='register'),
                  # for those template that don't have view we can render our template by template_name
                  path('login/', authenticate.LoginView.as_view(template_name='user/login.html'), name='login'),
                  path('logout/', authenticate.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
                  path('profile/', user_view.user_profile, name='profile'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,
                                                                                         document_root=settings.STATIC_ROOT)
