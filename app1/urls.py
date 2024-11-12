from django.urls import path
from . import views

urlpatterns=[
    path('fv/',views.First_view),
    path('sv/',views.Second_view),
]