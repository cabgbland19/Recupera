from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, MultiPartParser
from apps.userss.authentication_mixin  import Authentication
from apps.basses.api.serializers import *
from django.shortcuts import get_object_or_404
from apps.basses.models import *



class recoverViewset(Authentication,viewsets.ModelViewSet):
    serializer_class= recoverBaseSerializers
    parser_classes=(JSONParser,MultiPartParser)
    model=recoverBase

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.order_by('date')
    
    def list(self, request):
        recover_serializer = self.get_serializer(self.get_queryset(), many=True)
        data = {
            "total": self.get_queryset().count(),
            "totalNotFiltered": self.get_queryset().count(),
            "rows": recover_serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)


    def create(self, request):
        # send information to serializer 
       
        serializer = self.serializer_class(data=request.data)     
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'base field created succesfully!'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, pk):
        return get_object_or_404(self.model, pk=pk)

    def retrieve(self,request,pk):
        base = self.get_object(pk)

    def update(self, request, pk=None):
        base = self.get_object(pk)
        
        
        enviargtc_serializer = self.serializer_class(base, data=request.data)            
        if enviargtc_serializer.is_valid():
            enviargtc_serializer.save()
            return Response({'message':'Base updated succesfully!','data':enviargtc_serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'message':'', 'error':enviargtc_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class finalbaseViewset(Authentication,viewsets.ModelViewSet):
    serializer_class= finalBaseSerializer
    parser_classes=(JSONParser,MultiPartParser)
    model=finalBase

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.order_by('date')
    
    def list(self, request):
        recover_serializer = self.get_serializer(self.get_queryset(), many=True)
        data = {
            "total": self.get_queryset().count(),
            "totalNotFiltered": self.get_queryset().count(),
            "rows": recover_serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)


    def create(self, request):
        # send information to serializer 
       
        serializer = self.serializer_class(data=request.data)     
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'base field created succesfully!'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, pk):
        return get_object_or_404(self.model, pk=pk)

    def retrieve(self,request,pk):
        base = self.get_object(pk)

    def update(self, request, pk=None):
        base = self.get_object(pk)
        
        
        enviargtc_serializer = self.serializer_class(base, data=request.data)            
        if enviargtc_serializer.is_valid():
            enviargtc_serializer.save()
            return Response({'message':'Base updated succesfully!','data':enviargtc_serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'message':'', 'error':enviargtc_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


