from django.urls import path 
from .import views
urlpatterns = [
    path('',views.homePage,name="homePage"),
    path('contest',views.contestPage,name="contestPage")
]
