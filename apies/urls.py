from django.urls import path
from . import views

app_name = 'apies'

urlpatterns = [
    path('', views.get_weather, name='get_weather'),


]
