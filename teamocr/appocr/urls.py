from django.urls import path
from . import views

urlpatterns = [
    # Do nothing just take us to home
    path('', views.home, name="home"),
    path('text/', views.textConversions, name="text"),
    path('license/', views.license, name='license'),
]