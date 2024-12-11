from Home.views import index, people, login, PersonAPIView
from django.urls import path

urlpatterns = [
    path('index/', index),
    path('people/', people),
    path('login/', login),
    path('person-api-class/', PersonAPIView.as_view()),
]