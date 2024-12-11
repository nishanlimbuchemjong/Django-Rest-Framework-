from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET', 'POST'])
def index(request):
    courses = {
        'course_name': 'Python',
        'learn': ['flask', 'Django', 'FastApi'],
        'course_provider': 'Scaler'
    }
    if request.method == 'GET':
        print('you hit get method.')
        return Response(courses)
    elif request.method == 'POST':
        print('you hit post method.')
        return Response(courses)