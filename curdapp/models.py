from django.db import models

class StudentData(models.Model):
    student_roll_no=models.IntegerField(unique=True)
    student_first_name=models.CharField( max_length=100)
    student_last_name=models.CharField( max_length=100)




