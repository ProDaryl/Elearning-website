from django.db import models
from django.contrib.auth.models import User
from course_enlistment.models import Course

    
class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    enrolled_at = models.DateTimeField(auto_now_add=True)
    progress = models.FloatField(default=0.0)

    def __str__(self):
        return f'{self.user.username} - {self.course.title} - {self.progress}%'