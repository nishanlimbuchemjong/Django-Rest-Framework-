from Home.views import index, people, login
from django.urls import path

urlpatterns = [
    path('index/', index),
    path('people/', people),
    path('login/', login)
]