from django.db import models
class Student (models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    date_of_birth = models.CharField(max_length=25)
    codeID = models.PositiveSmallIntegerField()
    email = models.EmailField()
    nationality = models.CharField(max_length=25)
    bio = models.TextField()
    profile = models.ImageField()
    number_of_courses = models.PositiveSmallIntegerField()
    classes = models.CharField(max_length=25)
    guardians_name = models.CharField(max_length=20)
    place_of_residence = models.CharField(max_length=20)
    nationalId = models.PositiveSmallIntegerField()
    phone_number = models.PositiveIntegerField()
    KCSE_grade = models.CharField(max_length=20)
    medical_condition = models.TextField()
    room_number = models.PositiveSmallIntegerField
    
    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    
    

# Create your models here.

