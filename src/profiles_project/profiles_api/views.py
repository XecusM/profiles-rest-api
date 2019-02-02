from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from . import serializers
from . import models

# Create your views here.

class HelloApiView(APIView):
    '''
    Test API View.
    '''

    serializer_class = serializers.HelloSerializer

    def get(self, request, fromat=None):
        '''
        Returns a list of APIView featuers.
        '''

        an_apiview = [
            'Uses HTTP methods functions (get, post, patch, put, delete)',
            'It is a similar to a tranditional Django view',
            'Gives you the most control over your logic',
            'It mapped manually to URLS'
        ]

        return Response({'messege':'Hello!','an_apiview':an_apiview})

    def post(self, request):
        '''
        Create a hello message with our name.
        '''
        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {}'.format(name)
            return Response({'message' : message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        '''
        Handels updating an object
        '''
        return Response({'method':'put'})

    def patch(self, request, pk=None):
        '''
        Patch request, only updates fields provided in the request.
        '''
        return Response({'method':'patch'})

    def delete(self, request, pk=None):
        '''
        Delete an object.
        '''
        return Response({'method':'delete'})

class HelloViewSet(viewsets.ViewSet):
    '''
    Test API ViewSet.
    '''
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        '''
        Return Hello message.
        '''
        a_viewset=[
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLS using Routers',
            'Provides more functionality with less code.',
        ]

        return Response({'message':'Hello','a_viewset':a_viewset})

    def create(self, request):
        '''
        Create a hello message.
        '''
        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {}'.format(name)
            return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        '''
        Handels getiing an object by its ID
        '''

        return Response({'Http_method':'GET'})

    def update(self,request,pk=None):
        '''
        Handles updating an object
        '''

        return Response({'Http_method':'PUT'})

    def partial_update(self,request,pk=None):
        '''
        Handels update part of an object
        '''

        return Response({'Http_method':'PATCH'})

    def destroy(self,request,pk=None):
        '''
        Handles removing an object
        '''

        return Response({'Http_method':'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    '''
    Handles creating and updating profiles
    '''

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfiles.objects.all()
