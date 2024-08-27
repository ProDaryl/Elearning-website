from django.db import models

from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

class Module(models.Model):
    course = models.ForeignKey(Course, related_name='modules', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

class Content(models.Model):
    module = models.ForeignKey(Module, related_name='contents', on_delete=models.CASCADE)
    content_type = models.CharField(max_length=10, choices=(('pdf', 'PDF'), ('video', 'Video')))
    file = models.FileField(upload_to='course_content/')

    def __str__(self):
        return f'{self.module.title} - {self.content_type}'

class UserProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    completion_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} - {self.content.module.title} - {self.completed}'
