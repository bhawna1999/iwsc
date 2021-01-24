from django.urls import path
from . import views
from .views import *

from django.contrib.staticfiles.urls import staticfiles_urlpatterns


app_name = "main"
urlpatterns = [
	path('',views.home , name = "home"),
	path('about/' ,views.about , name = "about"),
    path('contact/', views.contact, name = "contact"), 
    path('blog/', views.blog, name='blog'), 
    
]


urlpatterns += staticfiles_urlpatterns()