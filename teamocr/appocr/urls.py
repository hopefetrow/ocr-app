from django.urls import path
from . import views

urlpatterns = [
    # Do nothing just take us to home
    path('', views.home, name="home"),
    path('text/', views.textConversions, name="text"),
    path('license/', views.license, name='license'),
    # Page that reads check number 
    path('check/', views.check, name='check'),

    # For testing purpose only 
    path('test/', views.test, name="test"),
    # Please comment the above line for final diployment 
]