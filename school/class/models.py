from django.db import models
class Class(models.Model):
    class_name=models.CharField(max_length=20)
    class_color=models.CharField(max_length=20)
    class_building_material=models.CharField(max_length=20)
    class_size=models.CharField(max_length=20)
    class_capacity=models.PositiveSmallIntegerField()
    class_lightning=models.CharField(max_length=20)
    class_temperature=models.CharField(max_length=20)
    class_odor=models.CharField(max_length=20)
    class_comfort=models.CharField(max_length=20)
    class_state=models.CharField(max_length=20)

    def __str__(self):
        return f"{self.class_name} {self.class_color}"

# Create your models here.
