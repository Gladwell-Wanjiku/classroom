from django.db import models

# Create your models here.
class Classroom(models.Model):
    class_name = models.CharField(max_length=20)
    students = models.CharField(max_length=20)
    size = models.PositiveIntegerField()
    location = models.CharField(max_length=20)
    max_capacity = models.PositiveBigIntegerField()
    class_number = models.PositiveSmallIntegerField()
    material = models.CharField(max_length=20)
    equipments = models.CharField(max_length=20)
    trainer = models.CharField(max_length=20)
