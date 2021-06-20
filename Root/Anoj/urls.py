from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.homePage, name="homePage"),
    path('contest', views.contestPage, name="contestPage"),
    path('ide',views.ide,name="ide")

]

# url(r'^(?P<slug>[\w])/$') then access as (request,slug)
