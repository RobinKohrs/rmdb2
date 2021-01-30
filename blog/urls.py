from django.urls import path
from . import views

# regex were used a lot to match the urls
urlpatterns = [
    path('', views.home, name="blog-home"), # empty path, views.home is the function, name is for reverse lookup for when we have multiple app
    path('about/', views.about, name="blog-about")
]