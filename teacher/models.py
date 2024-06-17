from django.db import models

# Create your models here.
class Teacher(models.Model):
    first_name=models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    email = models.EmailField()
    course = models.CharField(max_length=20)
    nationality = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    level_of_education =models.CharField(max_length=15)
    years_of_experience = models.PositiveSmallIntegerField()
    teaching_hours = models.DurationField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
