from django.urls import path
from .views import *
from step import views
urlpatterns= [
    path("", Index.as_view(), name='index') ,
    path('about/', About.as_view(), name="about" ) ,
    path('Contact/', Contact.as_view(), name="contact" ),
    path('weather/', views.weather, name='weze'),
]
