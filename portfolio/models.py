from django.db import models
from django.contrib.auth.models import User
from voting.models import Vote
from thumbs import ImageWithThumbsField

class Portfolio(models.Model):
    user = models.ForeignKey(User, unique=False)
    image = ImageWithThumbsField(upload_to='portfolio', sizes=( (48,48),(73,73),(190,125),(158,105),(223,223),(235,165) ) ,blank=True)
    creation_date = models.DateField(blank=True,null=True)
    last_modified = models.DateField(auto_now=True)
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