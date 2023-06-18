from django.db import models

# Create your models here.

class User(models.Model):
    name=models.CharField(max_length=255,null=False)
    date_of_birth =models.DateField(null=True , blank=True)

class Todo(models.Model):
    CHOICES=[
        ("L","LOW"),
        ("M","MEDIUM"),
        ("H","HIGH")
    ]
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    description=models.CharField(max_length=200)
    user =models.ForeignKey(User , on_delete=models.CASCADE)
    priority=models.CharField(max_length=1,choices=CHOICES)

