from rest_framework.decorators import api_view
from rest_framework.response import Response
from Home.serializer import PeopleSerializer, LoginSerializer, RegisterSerializer
from Home.models import Person
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.core.paginator import Paginator
from rest_framework.decorators import action

class LoginAPI(APIView):
    def post(self, request):
        data = request.data
        serializer = LoginSerializer(data=data)
        if not serializer.is_valid():
            return Response({
                'status': False,
                'message': serializer.errors,
            }, status.HTTP_400_BAD_REQUEST)
        user = authenticate(username=serializer.data['username'], password=serializer.data['password'])

        token = Token.objects.get_or_create(user=user)
        return Response({'status': True, 'message': 'user login', 'token': str(token)}, status.HTTP_201_CREATED)


class RegisterAPI(APIView):
    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=data)

        if not serializer.is_valid():
            return Response({
                'status': False,
                'message': serializer.errors,
            }, status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response({'status': True, 'message': 'user created'}, status.HTTP_201_CREATED)


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
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    def get(self, request):
        try:
            objs = Person.objects.all()
            page = int(request.GET.get('page', 1))
            page_size = 2
            paginator = Paginator(objs, page_size)
            serializer = PeopleSerializer(paginator.page(page), many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({
                'status': False,
                'message': 'Invalid page'
            })


    def post(self, request):
        data = request.data
        serializer = PeopleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def patch(self, request):
        data = request.data
        obj = Person.objects.get(id=data['id'])
        serializer = PeopleSerializer(obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request):
        data = request.data
        obj = Person.objects.get(id=data['id'])
        obj.delete()
        return Response({'message': 'person deleted'})

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

class PeopleViewSet(viewsets.ModelViewSet):
    serializer_class = PeopleSerializer
    queryset = Person.objects.all()
    http_method_name = ['get','post']
    # search functionality
    def list(self, request):
        search = request.GET.get('search')
        queryset = self.queryset
        if search:
            queryset = queryset.filter(name__startswith = search)
        serializer = PeopleSerializer(queryset, many=True)

        return Response({'status': 200, 'data': serializer.data}, status=status.HTTP_204_NO_CONTENT)

    # @action(detail=False, methods=['post'])
    # def send_mail_to_person(self, request):
    #     return Response({
    #         'status': True,
    #         'message': 'email sent succes'
    #     })

    @action(detail=True, methods=['GET'])
    def send_mail_to_person(self, request, pk):
        obj = Person.objects.get(pk=pk)
        serializer = PeopleSerializer(obj)
        print(pk)
        return Response({
            'status': True,
            'message': 'email sent succes',
            'data': serializer.data
        })
