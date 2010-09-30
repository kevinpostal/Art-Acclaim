from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.core.files.storage import default_storage as s3_storage
# Create your models here.

class Image_Tank(models.Model):
    user = models.ForeignKey(User, unique=False)
    image = models.FileField(storage=s3_storage,upload_to='tmp')
    creation_date = models.DateField(auto_now_add=True)
    type = models.CharField(max_length=100)
    hash = models.CharField(max_length=224)
    
    def photo_url(self):
    
        return '<img src = "%s%s" height="150" width="150"></img>' % (settings.MEDIA_URL,self.image)

    photo_url.allow_tags = True


import tasks