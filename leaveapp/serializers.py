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
        fields='__all__'
        read_only_fields=['id','head_name']

       
  
    def validate_start_date(self, data):
        if data <=datetime.now:
            return serializers.ValidationError("start date cannot be in past ")
        return data    

    def validate_end_date(self,data):
        if data>self.validate_start_date:
            return serializers.ValidationError("end_date cannot be before start date ")
        return data



