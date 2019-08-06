from django.db import models

# Create your models here.
class Job(models.Model):
    # Property of the admin web app
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)