from django.db import models

# Create your models here.
class Product(models.Model):
   #ref=models.CharField(max_length=4,primary_key=True )
   desciption=models.CharField(max_length=6)
   
   class Meta:
    db_table = 'p'
    managed = True
    verbose_name = 'p'
    verbose_name_plural = 'ps' 