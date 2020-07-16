from django.urls import path
from . import views

app_name = 'surgeonapp'

urlpatterns = [
    path('',views.home,name="home")
]