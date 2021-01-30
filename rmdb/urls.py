"""rmdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

# inclclude chopps of all the part of the url that was already matched. So he will pass "" -> to blog.urls which will resolve in the home page
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("blog.urls")) # This way we actually say that the "blog" urls are our home-page where we land initially whithout anything
]
