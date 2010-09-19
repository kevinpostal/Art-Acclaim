import re, datetime
from dateutil import relativedelta
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models import permalink
from django.contrib.auth.models import User
from django.contrib.localflavor.us.models import PhoneNumberField
from thumbs import ImageWithThumbsField

class Profile(models.Model):

    user = models.ForeignKey(User, unique=True)
    mugshot = ImageWithThumbsField(upload_to='mugshots', sizes=( (73,73),(190,190),(223,223),(325,325) ) ,blank=True) 
    #models.FileField(_('mugshot'), upload_to='mugshots', blank=True)
    location = models.CharField(_('location'), blank=True, max_length=100)
    quote = models.TextField(_('quote'), blank=True)
    education = models.TextField(_('education'), blank=True)
    bio = models.TextField(_('Bio'), blank=True)
    
    class Meta:
        verbose_name = _('user profile')
        verbose_name_plural = _('user profiles')
        db_table = 'user_profiles'

    def __unicode__(self):
        return u"%s" % self.user.get_full_name()

    @property
    def name(self):
        if self.user:
            return u"%s" % self.user.get_full_name()
        else:
            return None

    @permalink
    def get_absolute_url(self):
        return ('profile_detail', None, { 'username': self.user.username })

