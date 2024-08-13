from django.db import models
# from .models import Teacher
class Course(models.Model):
    course_name=models.CharField(max_length=20)
    course_description=models.TextField(max_length=20)
    course_level=models.CharField(max_length=20)
    course_duration=models.PositiveSmallIntegerField()
    course_objective=models.CharField(max_length=20)
    course_module=models.TextField(max_length=25)
    # course_prior_skills=models.Choices(max_length=25)
    course_learning_material=models.CharField(max_length=20)
    # course_trainer = models.OneToOneField(Teacher,on_delete=models.CASCADE)
    course_attendance_per_week=models.CharField(max_length=100, default=5)
    classes_hours = models.DurationField(max_length=5, default=2)
    assessment_requirements = models.CharField(max_length=255, default='Default Value Here')

    

    def __str__(self):
        return f"{self.course_name} {self.course_description}"
    

# Create your models here.
