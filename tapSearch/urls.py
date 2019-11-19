from django.urls import path
from tapSearch import views

app_name = 'tapsearch'
urlpatterns = [
    path('', views.index, name="index"),
    path('data', views.data, name="data")
]