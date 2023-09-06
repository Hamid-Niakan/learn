from django.urls import path
from . import views

urlpatterns = [
    path('hail/', views.say_hello),
]
