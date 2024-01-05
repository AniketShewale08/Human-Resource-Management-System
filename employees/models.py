from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length = 100)
    designation = models.CharField(max_length = 50)
    department = models.CharField(max_length = 50)
    date_of_joining = models.DateField()
    attendance = models.BooleanField(default = False)
    attendance_date = models.DateField(null = True, blank = True)

    def __str__(self) -> str:
        return self.name