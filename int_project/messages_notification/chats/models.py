from django.db import models
from datetime import datetime

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=1000)
class message(models.Model):
    message = models.CharField(max_length=200000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=200000)
    Course = models.CharField(max_length=200000)