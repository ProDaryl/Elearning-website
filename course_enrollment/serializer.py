from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Course, Enrollment

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields=['id','username', 'email']
class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Enrollment
        fields=['id','user','course']