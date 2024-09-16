from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from .models import Enrollment
from course_enlistment.models import Course
from .serializer import Userserializer,EnrollmentSerializer
from django.contrib.auth.models import User

# Create your views here
class EnrollView(APIView):
    # renderer_classes = [JSONRenderer]
    def get(self, request, course_id):
        enrollments = Enrollment.objects.all().values('user__username', 'course__title', 'enrolled_at', 'progress')
        return Response(enrollments, status=status.HTTP_200_OK)

    def post(self, request, course_id):
        # Fetch user and course IDs from request data
        # user_id = request.data.get('user_id')
        # course_id = request.data.get('course_id')

        # Validate the presence of user_id and course_id in request
        # if not user_id or not course_id:
        #     return Response({'error': 'User ID and Course ID are required.'}, status=status.HTTP_400_BAD_REQUEST)

        # Fetch the user and course objects
        user = request.user
        course = get_object_or_404(Course, id=course_id)

        # Check if the enrollment already exists or create a new one
        enrollment, created = Enrollment.objects.get_or_create(user=user, course=course)

        if not created:
            return Response({'error': 'User already enrolled in this course'}, status=status.HTTP_400_BAD_REQUEST)

        # Successful enrollment
        return Response({'message': 'User enrolled in this course successfully'}, status=status.HTTP_201_CREATED)

class UnenrollView(APIView):
    def post(self, request,):
        user_id =request.data.get('user_id')
        course_id =request.data.get('course_id')
        try:
            enrollment =Enrollment.objects.get(user_id=user_id,course_id=course_id)
        except Enrollment.DoesNotExist:
            return Response({'error': 'Enrollment not found'},status=status.HTTP_404_NOT_FOUND)
        enrollment.delete()
        return Response({'message': 'User unenrolled successfully'},status=status.HTTP_200_OK)
    
class EnrollmentListView(generics.ListAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
        
