from django.db import models
class Teacher(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    age = models.PositiveSmallIntegerField()
    gender = models.CharField(max_length=20)
    nationality = models.CharField(max_length=20)
    teacherID = models.PositiveSmallIntegerField()
    email = models.EmailField() 
    specialization = models.CharField(max_length=25)
    date_of_birth = models.DateField()
    years_of_experience = models.PositiveSmallIntegerField() 

    def __str__(self):
        return f"{self.firstname} {self.email}"

# Create your models here.
