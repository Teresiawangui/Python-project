from django.db import models
class Student (models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.EmailField()
    country = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    code = models.PositiveSmallIntegerField()
    
    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    
    

# Create your models here.

