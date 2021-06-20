
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from Compiler import views
from django.views.decorators.csrf import csrf_exempt 
urlpatterns = [
    path('snippets/',csrf_exempt(views.CompilerList.as_view())),
    path('<slug:slug>/login',views.login,name='login'),
    path('<slug:slug>/logout',views.logout,name='logout'),
    path('<slug:slug>',views.fetchpage,name="fetch")
]