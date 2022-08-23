from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from .models import User
from .serializers import RegistrationSerializer
from rest_framework import generics
from rest_framework import serializers
import uuid

# Create your views here.
# class UserList(APIView):
#     """
#     List all Users, or create a new User object.
#     """
    
#     def post(self, request, format=None):
#         serializer = UserSerializer(data = request.data)
#         if serializer.is_valid():
#             first_name = request.data.get('first_name')
#             last_name = request.data.get('last_name')
#             username = first_name + last_name
#             data = serializer.save()
#             data.username = username + '-'+ str(data.id)
#             data.password = make_password(request.data.get('password'))
#             data.is_active = True
#             data.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RegistrationAPIView(generics.GenericAPIView):

    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response({
                "RequestId": str(uuid.uuid4()),
                "Message": "User created successfully",
                
                "User": serializer.data}, status=status.HTTP_201_CREATED
                )
        
        return Response(status=status.HTTP_400_BAD_REQUEST)
        #return Response({"Errors": serializers.errors}, status=status.HTTP_400_BAD_REQUEST)