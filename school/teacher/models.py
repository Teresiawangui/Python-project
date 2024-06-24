from django.db import models
class Teacher(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=20)
    nationality = models.CharField(max_length=20)
    teacherID = models.PositiveSmallIntegerField()
    email = models.EmailField() 
    specialization = models.CharField(max_length=25)
    number_of_classes_per_week = models.PositiveSmallIntegerField()
    years_of_experience = models.PositiveSmallIntegerField()
    bio = models.TextField()
    contact = models.CharField(max_length=20)
    bank_account_number = models.TextField()
    profile = models.ImageField()
    phone_number = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.firstname} {self.email}"

# Create your models here.
