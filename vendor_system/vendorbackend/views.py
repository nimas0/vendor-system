from django.shortcuts import render, HttpResponse
from rest_framework.serializers import Serializer
from .models import Photographer
from .serializers import PhotographerSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.

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
