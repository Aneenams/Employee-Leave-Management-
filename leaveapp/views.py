from django.shortcuts import render

from django.contrib.auth.models import User
from leaveapp.models import Leave
from leaveapp.serializers import UserSerializer,LeaveSerializer
from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from rest_framework import authentication ,permissions
# Create your views here.

class UserRegisterListView(CreateAPIView):
    serializer_class=UserSerializer

class LeaveCreateListView(CreateAPIView,ListAPIView):
    serializer_class=LeaveSerializer
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(head_name=self.request.user)
        return ("created successfully")

    def get_queryset(self):
        queryset=Leave.objects.filter(head_name=self.request.user)
        return queryset




class LeaveDetailView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):
    serializer_class=LeaveSerializer
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Leave.objects.filter(head_name=self.request.user)



     


        
  

    