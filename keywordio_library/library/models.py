from django.db import models

# Create your models here.
from django.db import models  
class Library(models.Model):  
    eid = models.CharField(max_length=100 , primary_key=False)  
    name = models.CharField(max_length=100)  
    author = models.CharField(max_length=100)  
    year = models.IntegerField()  
    class Meta:  
        db_table = "library"  