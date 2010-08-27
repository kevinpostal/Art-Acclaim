from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Portfolio(models.Model):
    user = models.ForeignKey(User, unique=False)
    image = models.FileField(upload_to='portfolio', blank=True)
    creation_date = models.DateField(blank=True,null=True)
    last_modified = models.DateField(auto_now=True)
    title = models.CharField(max_length=300)
    dimensions = models.CharField(max_length=100,blank=True)
    materials = models.CharField(max_length=100,blank=True)
    
    def __unicode__(self):
        return u'%s [user: %s]' % (self.title, self.user.id)