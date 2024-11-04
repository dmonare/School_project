from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    grade = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name}"

class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)
    years_of_experience = models.IntegerField()
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.first_name}"

class Class(models.Model):
    name = models.CharField(max_length=20)
    start_date = models.DateField()
    end_date  = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}"
