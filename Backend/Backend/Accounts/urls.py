from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from Accounts import views


urlpatterns = [
    path('login', views.UserList.as_view()),
    path("login/<str:userName>,<str:password>/", views.UserList.as_view())
]
urlpatterns = format_suffix_patterns(urlpatterns)