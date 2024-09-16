from django.test import TestCase
from django.contrib.auth.models import User
from .models import Course

class CourseEnrollmentSignalTest(TestCase):

    def setUp(self):
        # Create a test course where users will be automatically enrolled
        self.course = Course.objects.create(name='Python 101', description='Intro to Python')

    def test_user_auto_enrolled_in_course_on_creation(self):
        # Create a new user
        new_user = User.objects.create_user(username='newuser', password='newpass')

        # Check if the user is automatically enrolled in the course
        self.assertIn(new_user, self.course.students.all())
        self.assertEqual(self.course.students.count(), 1)
    
    def test_multiple_users_auto_enrolled(self):
        # Create multiple users
        user1 = User.objects.create_user(username='user1', password='pass1')
        user2 = User.objects.create_user(username='user2', password='pass2')

        # Check if both users are enrolled
        self.assertIn(user1, self.course.students.all())
        self.assertIn(user2, self.course.students.all())
        self.assertEqual(self.course.students.count(), 2)