from django.db import models

class Myusers(models.Model):
    userId=models.AutoField(primary_key=True)
    userName=models.CharField(max_length=30)
    userEmail=models.EmailField()
    userPassword=models.CharField(max_length=12)

class Track(models.Model):
    name = models.CharField(max_length=40)


class Trainee(models.Model):
    name = models.CharField(max_length=40)
    track_name = models.ForeignKey(Track, on_delete=models.CASCADE)