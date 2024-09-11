from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Enrollment
from course_enlistment.models import Course
from .serializer import Userserializer,EnrollmentSerializer
from django.contrib.auth.models import User

# Create your views here
class EnrollView(APIView):
    def post(self, request):
        user_id =request.data.get('user_id')
        course_id =request.data.get('course_id')
        try:
            user =User.objects.get(id=user_id)
            course =Course.objects.get(id=course_id)
        except User.DoesNotExist:
            return Response({'error': 'User not found'},status=status.HTTP_404_NOT_FOUND)
        except Course.DoesNotExist:
            return Response({'error':'Course not found'},status=status.HTTP_404_NOT_FOUND)
        enrollment, created =Enrollment.objects.get_or_created(user=user,course=course)
        if not created:
            return Response({'error': 'User already enrolled in this course'},status=status.HTTP_404_BAD_REQUEST)
        return Response({'message': 'User already enrolled in this course successfully'},status=status.HTTP_201_CREATED)

class UnenrollView(APIView):
    def post(self, request):
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
        
