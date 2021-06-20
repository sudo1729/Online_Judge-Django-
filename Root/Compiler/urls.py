
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from Compiler import views

urlpatterns = [
    path('snippets/', views.CompilerList.as_view()),
    path('<slug:slug>/login',views.login,name='login'),
    path('<slug:slug>/logout',views.logout,name='logout'),
    path('<slug:slug>',views.check,name="check")
]

urlpatterns = format_suffix_patterns(urlpatterns)