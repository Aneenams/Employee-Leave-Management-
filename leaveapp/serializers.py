from rest_framework import serializers
from django.contrib.auth.models import User
from leaveapp.models import Leave
from datetime import datetime, timedelta 

class UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)

    class Meta:
        model=User
        fields=['id','username','email','password']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class LeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model=Leave
        fields=['employee_name','reason','start_date','end_date','leave_type']
        read_only_fields=['id','hr_name']

       
  
    # def validate_start_date(self, data):
    #     if data<=2025:
    #         return serializers.ValidationError("start date cannot be in past ")
    #     return data    

    # def validate_end_date(self,data):
    #     if data>self.validate_start_date:
    #         return serializers.ValidationError("end_date cannot be before start date ")
    #     return data



