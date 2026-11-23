from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Teacher(User):
    mat=models.CharField(max_length=6,unique=True)
    
    class Meta:
        db_table = 'ens'
        managed = True
        verbose_name = 'ens'
        verbose_name_plural = 'Teachers'
 
     