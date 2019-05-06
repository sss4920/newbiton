"""busking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
import lendapp.views
import service1.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('theme.urls')),
    path('home/', lendapp.views.home, name = "home"),
    path('lend/new', lendapp.views.new, name = "new"),
    path('lend/<int:post_id>/', lendapp.views.content, name = "content"),
    path('lend/postcreate', lendapp.views.postcreate, name = "postcreate"),
    path('service1/place', service1.views.place, name = "place"),
    path('service1/player', service1.views.player, name="player"),
    
]
