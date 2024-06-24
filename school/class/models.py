from django.db import models
class Class(models.Model):
    class_name=models.CharField(max_length=20)
    class_courses =models.CharField()
    class_representative = models.CharField()
    class_size=models.CharField(max_length=20)
    class_capacity=models.PositiveSmallIntegerField()
    room_number = models.CharField()
    class_vision = models.TextField()
    class_mission = models.TextField()
    class_enrollment = models.CharField(max_length=20)
    class_artwork = models.CharField(max_length=20)
    color_of_chairs = models.CharField(max_length=25)
    number_of_laptops =models.PositiveSmallIntegerField()
    number_of_windows = models.PositiveSmallIntegerField()
    number_of_television = models.PositiveSmallIntegerField()
    number_of_electronic_equipments = models.PositiveSmallIntegerField() 

    def __str__(self):
        return f"{self.class_name} {self.class_color}"

# Create your models here.
