from django.db import models

# Create your models here.
class Student(models.Model):
    student_name = models.CharField(max_length=25)
    student_email = models.EmailField()
    student_bio = models.TextField()
    student_nationality = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    code = models.PositiveSmallIntegerField()
    student_guardian = models.CharField()
    student_lock_number = models.IntegerField()
    student_class = models.CharField(max_length=20)
    student_mentor = models.CharField(max_length=20)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"