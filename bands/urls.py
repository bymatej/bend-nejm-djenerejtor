from django.urls import path

from . import views

urlpatterns = [
    path('name', views.get_random_name, name='get_random_name'),
]
