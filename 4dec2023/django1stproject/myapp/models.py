from django.db import models

class registermodel(models.Model):
    username=models.CharField(max_length=100)
    email = models.EmailField()
    dob = models.DateField(max_length=100)
    gender = models.CharField(max_length=100)

