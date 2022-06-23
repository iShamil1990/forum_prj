from tokenize import Name
from django.shortcuts import render
from rest_framework import viewsets
from api import serializers
from api.models import Checkbox
from api.serializers import CheckboxSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework import authentication, permissions
from rest_framework import generics, mixins

# class CheckboxViewSet(viewsets.ModelViewSet):
#     queryset = Checkbox.objects.all()
#     serializer_class = CheckboxSerializer

class CheckboxList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Checkbox.objects.all()
    serializer_class = CheckboxSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

@api_view(['GET'])
def checkbox_list(req):
    checkboxes = Checkbox.objects.all()
    serializer = CheckboxSerializer(checkboxes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def checkbox_detail(req, pk):
    try:
        checkbox = Checkbox.objects.get(id=pk)
        serializer = CheckboxSerializer(checkbox)
    except Checkbox.DoesNotExist:
        return Response({"error": f"Checkbox with id={pk} is not found"}, status = status.HTTP_404_NOT_FOUND)
    return Response(serializer.data)

@api_view(['POST'])
def checkbox_create(req):
        serializer = CheckboxSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT'])
def checkbox_update(req, pk):
    try:
        checkbox = Checkbox.objects.get(id=pk)
        serializer = CheckboxSerializer(checkbox, data=req.data)
        if serializer.is_valid():
            serializer.save()
    except Checkbox.DoesNotExist:
        return Response({"error": f"Checkbox with id={pk} is not found"}, status = status.HTTP_404_NOT_FOUND)
    return Response(serializer.data)

@api_view(['DELETE'])
def checkbox_delete(req, pk):
    checkbox = Checkbox.objects.get(id=pk)
    checkbox.delete()
    # serializer = CheckboxSerializer(checkbox, data=req.data)
    return Response(status=status.HTTP_204_NO_CONTENT)
