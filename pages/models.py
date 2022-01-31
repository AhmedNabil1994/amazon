from django.db import models

class Myusers(models.Model):
    userId=models.AutoField(primary_key=True)
    userName=models.CharField(max_length=30)
    userEmail=models.EmailField()
    userPassword=models.CharField(max_length=8)

