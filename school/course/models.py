from django.db import models
class Course(models.Model):
    course_name=models.CharField(max_length=20)
    course_description=models.CharField(max_length=20)
    course_level=models.CharField(max_length=20)
    course_duration=models.PositiveSmallIntegerField()
    course_objective=models.CharField(max_length=20)
    course_module=models.CharField(max_length=25)
    course_prior_skills=models.CharField(max_length=25)
    course_attendance=models.PositiveSmallIntegerField()
    course_learning_material=models.CharField(max_length=20)
    course_trainer=models.CharField(max_length=25)

    def __str__(self):
        return f"{self.course_name} {self.course_description}"
    

# Create your models here.
