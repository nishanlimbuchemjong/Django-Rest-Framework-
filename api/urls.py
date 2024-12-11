from Home.views import index, people
from django.urls import path

urlpatterns = [
    path('index/', index),
    path('people/', people)
]