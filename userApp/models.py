from django.db import models
from django.contrib.auth.models import User

class CourseSelection(models.Model):
    COURSE_CHOICES = [
        ('c', 'C'),
        ('cpp', 'C++'),
        ('python', 'Python'),
        ('java', 'Java'),
        ('golang', 'Golang'),
    ]

    course = models.CharField(max_length=10, choices=COURSE_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    submission_date = models.DateTimeField(auto_now_add=True)