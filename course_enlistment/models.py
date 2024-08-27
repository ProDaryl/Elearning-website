from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    instructor = models.CharField(max_length=100)

    def __str__(self):
        return self.title
