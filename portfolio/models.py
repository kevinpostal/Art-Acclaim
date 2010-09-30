from django.db import models
from django.contrib.auth.models import User
from voting.models import Vote
from thumbs import ImageWithThumbsField
from django.core.files.storage import default_storage as s3_storage

class Portfolio(models.Model):
    user = models.ForeignKey(User, unique=False)
    image = ImageWithThumbsField(storage=s3_storage,upload_to='portfolio', sizes=( (48,48),(73,73),(190,125),(158,105),(223,223),(235,165),(325,325) ) ,blank=True)
    creation_date = models.DateTimeField(blank=True,null=True)
    last_modified = models.DateTimeField(auto_now=True)
    add_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=300)
    dimensions = models.CharField(max_length=100,blank=True)
    materials = models.CharField(max_length=100,blank=True)
    hash =  models.CharField(max_length=300)
    
    
    def _get_vote(self):
        "Returns the objects's score"
        return Vote.objects.get_score(self)
    vote = property(_get_vote)
    
    
    def __unicode__(self):
        return u'%s [user: %s]' % (self.title, self.user.id)
