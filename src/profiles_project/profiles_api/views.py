from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class HelloApiView(APIView):
    '''
    Test API View.
    '''

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
