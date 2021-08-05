#from django.db.models.query import QuerySet
#from django.shortcuts import render, HttpResponse
#from rest_framework.serializers import Serializer
#from django.http import JsonResponse
#from rest_framework.parsers import JSONParser
#from rest_framework.response import Response
#from rest_framework.decorators import api_view
#from rest_framework import status
#from rest_framework.views import APIView
#from rest_framework import generics
#from rest_framework import mixins
#from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from .models import Photographer
from .serializers import PhotographerSerializer, UserSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

# Create your views here.



class PhotographerViewSet(viewsets.ModelViewSet):
    queryset = Photographer.objects.all()
    serializer_class = PhotographerSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


'''
class PhotographerViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin
, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Photographer.objects.all()
    serializer_class = PhotographerSerializer
'''


'''
class PhotographerViewSet(viewsets.ViewSet):

    def list(self, request):
        photographers = Photographer.objects.all()
        serializer = PhotographerSerializer(photographers, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = PhotographerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        

    def retrieve(self, request, pk=None):
        queryset = Photographer.objects.all()
        photographer = get_object_or_404(queryset, pk=pk)
        serializer = PhotographerSerializer(photographer)
        return Response(serializer.data)

    def update(self, request, pk=None):
        photographer = Photographer.objects.get(pk=pk)

        serializer = PhotographerSerializer(photographer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        photographer = Photographer.objects.get(pk=pk)
        photographer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


'''


'''
class PhotographerList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Photographer.objects.all()
    serializer_class = PhotographerSerializer

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)

class PhotographerDetails(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Photographer.objects.all()
    serializer_class = PhotographerSerializer

    lookup_field = 'vendor_id'

    def get(self, request, vendor_id):
        return self.retrieve(request, vendor_id=vendor_id)

    def put(self, request, vendor_id):
        return self.update(request, vendor_id=vendor_id)
    
    def delete(self, request, vendor_id):
        return self.destroy(request, vendor_id=vendor_id)
'''


'''
class PhotographerList(APIView):

    def get(self, request):
        photographers = Photographer.objects.all()
        serializer = PhotographerSerializer(photographers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PhotographerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PhotographerDetails(APIView):
    
    def get_object(self, id):
        try:
            return Photographer.objects.get(vendor_id=id)
        except Photographer.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request, id):
        photographer = self.get_object(id)
        serializer = PhotographerSerializer(photographer)
        return Response(serializer.data)

    def put(self, request, id):
        photographer = self.get_object(id)
        serializer = PhotographerSerializer(photographer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        photographer = self.get_object(id)
        photographer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''


'''
@api_view(['GET','POST'])
def photographer_list(request):
    
    if request.method == 'GET':
        photographers = Photographer.objects.all()
        serializer = PhotographerSerializer(photographers, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = PhotographerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def photographer_details(request, pk):
    try:
        photographer = Photographer.objects.get(pk=pk)
    except Photographer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PhotographerSerializer(photographer)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = PhotographerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        photographer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''