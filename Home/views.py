from rest_framework.decorators import api_view
from rest_framework.response import Response
from Home.serializer import PeopleSerializer, LoginSerializer
from Home.models import Person
from rest_framework.views import APIView


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


@api_view(['POST'])
def login(request):
    data = request.data
    serializer = LoginSerializer(data=data)
    if serializer.is_valid():
        data = serializer.data
        print(data)
        return Response({'mesage': 'success'})
    return Response(serializer.errors)

class PersonAPIView(APIView):
    def get(self, request):
        objs = Person.objects.filter(color__isnull=False)
        serializer = PeopleSerializer(objs, many=True)
        return Response(serializer.data)
        return Response({'message': 'This is a GET request'})

    def post(self, request):
        data = request.data
        serializer = PeopleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
        return Response({'message': 'This is a POST request'})


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def people(request):
    if request.method == 'GET':
        objs = Person.objects.filter(color__isnull=False)
        serializer = PeopleSerializer(objs, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = request.data
        serializer = PeopleSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    elif request.method == 'PUT':
        data = request.data
        serializer = PeopleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    elif request.method == 'PATCH':
        data = request.data
        obj = Person.objects.get(id=data['id'])
        serializer = PeopleSerializer(obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    else:
        data = request.data
        obj = Person.objects.get(id=data['id'])
        obj.delete()
        return Response({'message': 'person deleted'})

