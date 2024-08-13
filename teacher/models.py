from django.db import models
# from .models import Course
class Teacher(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=20)
    nationality = models.CharField(max_length=20)
    teacherID = models.PositiveSmallIntegerField()
    email = models.EmailField() 
    specialization = models.CharField(max_length=25)
    # number_of_classes_per_week = models.ManyToManyField(Course, on_Delete=models.CASCADE )
    years_of_experience = models.PositiveSmallIntegerField()
    bio = models.TextField(default='')
    contact = models.CharField(max_length=20,default='075634252693')
    bank_account_number = models.TextField(default=456765)
    profile = models.ImageField(default='')
    phone_number = models.PositiveIntegerField(default='078654323412')

    def __str__(self):
        return f"{self.firstname} {self.email}"

# Create your models here.
