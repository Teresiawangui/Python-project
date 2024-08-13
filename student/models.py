from django.db import models
# from .models import Course
# from .models import Class
class Student (models.Model):
    # courses =models.ManyToManyField(Course)
    # firstname = models.OneToOneField(Class,on_delete=models.CASCADE)
    lastname = models.CharField(max_length=20)
    date_of_birth = models.CharField(max_length=25)
    codeID = models.CharField(max_length=100)  # Example definition
    email = models.EmailField()
    nationality = models.CharField(max_length=25)
    bio = models.TextField()
    profile = models.ImageField()
    number_of_courses = models.PositiveSmallIntegerField()
    classes = models.CharField(max_length=20 )
    guardians_name = models.CharField(max_length=20)
    place_of_residence = models.CharField(max_length=20)
    nationalId = models.PositiveSmallIntegerField()
    phone_number = models.PositiveIntegerField()
    KCSE_grade = models.CharField(max_length=20)
    medical_condition = models.TextField()
    room_number = models.PositiveSmallIntegerField
    
    def __str__(self):
        return f"{self.email} {self.lastname} {self.date_of_birth}"
    
   
# Create your models here.

