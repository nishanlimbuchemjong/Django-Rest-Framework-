from rest_framework.decorators import api_view
from rest_framework.response import Response
from Home.serializer import PeopleSerializer
from Home.models import Person


# Create your views here.
@api_view(['GET', 'POST'])
def index(request):

    if request.method == 'GET':
        json_response = {
            'name': 'Scaler',
            'courses': ['Python', 'C++'],
            'method': 'GET'
        }
    else:
        data = request.data
        print(data)
        json_response = {
            'name': 'Scaler',
            'courses': ['Python', 'C++'],
            'method': 'GET'
        }
    return Response(json_response)

@api_view(['GET', 'POST'])
def people(request):
    if request.method == 'GET':
        objs = Person.objects.all()
        serializer = PeopleSerializer(objs, many=True)
        return Response(serializer.data)

    else:
        data = request.data
        serializer = PeopleSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
