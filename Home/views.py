from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def index(request):
    courses = {
        'course_name': 'Python',
        'learn': ['flask', 'Django', 'FastApi'],
        'course_provider': 'Scaler'
    }
    return Response(courses)