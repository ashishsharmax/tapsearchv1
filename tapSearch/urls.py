from django.urls import path
from tapSearch import views

urlpatterns = [
    path('', views.index, name="index"),
]