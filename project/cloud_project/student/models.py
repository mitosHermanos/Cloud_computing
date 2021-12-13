from django.db import models
from django.utils import timezone

class Student(models.Model):
    name = models.CharField(null=False, max_length=100)
    surname = models.CharField(null=False, max_length=100)
    date_of_enrolment = models.DateTimeField(default=timezone.now)
    scholarship = models.BooleanField(default=False)
    age = models.IntegerField()
