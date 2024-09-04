from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    title= models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
class Enrollment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}enrolled in {self.course.title}"