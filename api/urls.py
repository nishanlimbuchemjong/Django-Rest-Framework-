from Home.views import index, people, login, PersonAPIView, PeopleViewSet, RegisterAPI, LoginAPI
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'peoples', PeopleViewSet, basename='peoples')
urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),
    path('index/', index),
    path('register/', RegisterAPI.as_view()),
    path('login/', LoginAPI.as_view()),
    path('people/', people),
    path('login/', login),
    path('person-api-class/', PersonAPIView.as_view()),
]