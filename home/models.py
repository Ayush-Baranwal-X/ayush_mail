from django.db import models
from django.utils import timezone

# Create your models here.

class Info(models.Model):
    name = models.CharField(max_length=100,null=True)
    email = models.CharField(max_length=100,null=True)
    username = models.CharField(max_length=100,null=True)
    gender = models.CharField(max_length=30,null=True)
    phone = models.CharField(max_length=10,null=True)
    country = models.CharField(max_length=30,null=True)
    date = models.DateTimeField()

    def __str__(self):
        return self.username

class Feedback(models.Model):
    name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)
    comment = models.TextField(null=True)
    date = models.DateTimeField()

    def __str__(self):
        return self.name
    
class Mail(models.Model):
    fromuser = models.CharField(max_length=100)
    touser = models.CharField(max_length=100)
    subject = models.CharField(max_length=200)
    deleteFrom = models.CharField(max_length=10,default='0')
    deleteTo = models.CharField(max_length=10,default='0')
    body = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.subject
    
