from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    title= models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    enrolled_at = models.DateTimeField(auto_now_add=True)
    progress = models.FloatField(default=0.0)

    def __str__(self):
        return f'{self.user.username} - {self.course.title} - {self.progress}%'