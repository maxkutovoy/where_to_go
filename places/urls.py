from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('plases/<int:place_id>/', views.about_place, name='about-place')
]
