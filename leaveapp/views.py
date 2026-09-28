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
        serializer.save(hr_name=self.request.user)

    def get_queryset(self):
        queryset=Leave.objects.filter(hr_name=self.request.user)

        # start_date=self.request.query_params.get('start_date')
        # if start_date:
        #     queryset=queryset.filter(start_date=start_date)

        # end_date=self.request.query_params.get('end_date')
        # if end_date<start_date:
        #     raise ValueError("end date cannot be before starting date")



        return queryset




class LeaveDetailView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):
    def get_queryset(self):
        return Leave.objects.filter(hr_name=self.request.user)



     


        
  

    