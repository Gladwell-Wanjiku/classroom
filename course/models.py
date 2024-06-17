from django.db import models

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=20)
    trainer = models.CharField(max_length=20)
    duration = models.PositiveBigIntegerField()
    assessments = models.PositiveIntegerField()
    syllabus = models.CharField(max_length=20)
    assignment = models.PositiveSmallIntegerField()
    course_id = models.PositiveIntegerField()
    description = models.TextField(max_length=20)
    prerequisites = models.CharField(max_length=20)
    resources = models.CharField(max_length=20)
    
