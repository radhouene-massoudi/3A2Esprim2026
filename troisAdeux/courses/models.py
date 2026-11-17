from django.db import models

# Create your models here.
class Courses(models.Model):
    nam=models.CharField(max_length=7)
    teacher=models.ForeignKey(
        'teacher.Teacher',
        related_name='courses',
        on_delete=models.CASCADE
    )