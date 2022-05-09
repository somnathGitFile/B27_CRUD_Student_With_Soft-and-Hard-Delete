from django.db import models

# Create your models here.
class Student(models.Model):
    sid = models.IntegerField()
    sname = models.CharField(max_length=100)
    smarks = models.FloatField()
    sadd = models.CharField(max_length=150)
    status = models.BooleanField(default=True)


