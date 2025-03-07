from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from rest_framework import viewsets
from profiles_api import models
from rest_framework.authentication import TokenAuthentication
from profiles_api import permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework import filters

class HelloApiView(APIView):
    """test api view"""
    serializer_class=serializers.HelloSerializer

    def get(self,request,format=None):
        an_apiview=[
            'use HTTP methods as function',
            'similar to traditional django view',
            'gives control over application logic',
            'mapped manualy to urls',
        ]

        return Response({'message':'Hello!','an_apiview':an_apiview})


    def post(self,request):
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message= f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST 
            )
    
    def put(self,request,pk=None):
        return Response({'method':'PUT'})
    
    def patch(self,request,pk=None):
        return Response({'method':'PATCH'})
    
    def delete(self,request,pk=None):
        return Response({'method':'DELETE'})
    

class HelloViewSets(viewsets.ViewSet):
    serializer_class=serializers.HelloSerializer

    def list(self,request):
        a_viewset=[
            'Uses actions (list,create,retrieve,update,partial_update)',
            'Automaticaly maps to urls using routers',
            'Provides more functionality with less code',
        ]

        return Response({'message': 'Hello!','a_viewsets':a_viewset})

    def create(self,request):
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def retrieve(self,request,pk=None):
        return Response({'http_method':'GET'})
    
    def update(self,request,pk=None):
        return Response({'http_method':'PUT'})
    
    def partial_update(self,request,pk=None):
        return Response({'http_method':'PATCH'})
    
    def delete(self,request,pk=None):
        return Response({'http_method':'DELETE'})
    
class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class UserLoginApiView(ObtainAuthToken):
    '''handle creating user authentication tokens'''

    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES






   