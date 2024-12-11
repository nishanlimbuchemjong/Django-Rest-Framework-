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
        print('you hit GET method.')
        return Response(courses)
    elif request.method == 'POST':
        print('you hit POST method.')
        return Response(courses)
    elif request.method == 'POST':
        print('you hit PUT method.')
        return Response(courses)