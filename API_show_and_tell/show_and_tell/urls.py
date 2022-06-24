from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.index),
    path('colorized/', views.colorizer),
    path('text_to_img/', views.text_to_img),
]