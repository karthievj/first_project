from django.urls import path
from . import views

urlpatterns = [
    #homepage
    path('homePage/', views.homePage, name='homepage'),
]