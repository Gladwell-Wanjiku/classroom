from django.db import models

# Create your models here.
class Teacher(models.Model):
    first_name=models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    date_of_birth = models.IntegerField()
    email = models.EmailField()
    teachers_resume= models.TextField()
    account_number = models.PositiveBigIntegerField()
    national_id = models.PositiveBigIntegerField()
    phone_number = models.IntegerField()
    teaching = models.DurationField()
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
