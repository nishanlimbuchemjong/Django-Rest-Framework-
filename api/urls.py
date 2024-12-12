from Home.views import index, people, login, PersonAPIView, PeopleViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'peoples', PeopleViewSet, basename='peoples')
urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),
    path('index/', index),
    path('people/', people),
    path('login/', login),
    path('person-api-class/', PersonAPIView.as_view()),
]