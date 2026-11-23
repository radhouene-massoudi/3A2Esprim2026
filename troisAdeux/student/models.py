from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Student(User):
    card=models.CharField(max_length=8,db_column='t')
    class Meta:
        db_table = 'student'
        managed = True
        verbose_name = 'student'
        verbose_name_plural = 'students'