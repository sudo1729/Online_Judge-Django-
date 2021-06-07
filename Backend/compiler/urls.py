from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from compiler import views

urlpatterns = [
    path('compiler/', views.CompilerList.as_view()),
    path('compiler/<int:pk>/', views.CompilerDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)