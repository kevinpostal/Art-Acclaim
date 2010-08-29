from django.db import models
from django.contrib.auth.models import User
from voting.models import Vote
        
class Portfolio(models.Model):
    user = models.ForeignKey(User, unique=False)
    image = models.FileField(upload_to='portfolio', blank=True)
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