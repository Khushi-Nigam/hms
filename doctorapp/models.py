from django.db import models

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=30)
    image=models.FileField(max_length=500)
    category=models.CharField(max_length=50)
    summary=models.TextField(max_length=200)
    content=models.TextField(max_length=500)