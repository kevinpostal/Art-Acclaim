from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Art_Work(models.Model):
    user = models.ForeignKey(User, unique=False)
    image = models.FileField(upload_to='art_works', blank=True)
    creation_date = models.DateField(blank=True)
    last_modified = models.DateField(auto_now=True)
    title = models.CharField(max_length=300)
    dimensions = models.CharField(max_length=100,blank=True)
    materials = models.CharField(max_length=100,blank=True)
