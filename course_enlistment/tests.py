from django.test import TestCase
from django.contrib.auth.models import User
from .models import Course, Module, Content, UserProgress
from django.urls import reverse

class CourseModelTest(TestCase):
    def setUp(self):
        self.course = Course.objects.create(title="Test Course", description="Test Description")
        self.module = Module.objects.create(course=self.course, title="Test Module", description="Test Module Description")
        self.content_pdf = Content.objects.create(module=self.module, content_type='pdf', file='test.pdf')
        self.content_video = Content.objects.create(module=self.module, content_type='video', file='test.mp4')
        self.user = User.objects.create_user(username='testuser', password='12345')
    
    def test_course_creation(self):
        self.assertEqual(self.course.title, "Test Course")
        self.assertEqual(self.course.description, "Test Description")

    def test_module_creation(self):
        self.assertEqual(self.module.title, "Test Module")
        self.assertEqual(self.module.description, "Test Module Description")
        self.assertEqual(self.module.course, self.course)

    def test_content_creation(self):
        self.assertEqual(self.content_pdf.content_type, 'pdf')
        self.assertEqual(self.content_video.content_type, 'video')
        self.assertEqual(self.content_pdf.module, self.module)
        self.assertEqual(self.content_video.module, self.module)

class CourseViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.course = Course.objects.create(title="Test Course", description="Test Description")
        self.module = Module.objects.create(course=self.course, title="Test Module", description="Test Module Description")
        self.content = Content.objects.create(module=self.module, content_type='pdf', file='test.pdf')
        self.client.login(username='testuser', password='12345')

    def test_course_list_view(self):
        response = self.client.get(reverse('course_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.course.title)
        self.assertTemplateUsed(response, 'courses/course_list.html')

    def test_course_detail_view(self):
        response = self.client.get(reverse('course_detail', args=[self.course.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.course.title)
        self.assertContains(response, self.module.title)
        self.assertTemplateUsed(response, 'courses/course_detail.html')

    def test_track_progress_view(self):
        response = self.client.get(reverse('track_progress', args=[self.content.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.content.content_type)
        self.assertTemplateUsed(response, 'courses/progress.html')

    def test_mark_as_completed(self):
        response = self.client.post(reverse('track_progress', args=[self.content.id]))
        progress = UserProgress.objects.get(user=self.user, content=self.content)
        self.assertTrue(progress.completed)
        self.assertEqual(response.status_code, 200)
