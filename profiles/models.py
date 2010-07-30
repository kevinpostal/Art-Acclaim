import re, datetime
from dateutil import relativedelta

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models import permalink
from django.contrib.auth.models import User
from django.contrib.localflavor.us.models import PhoneNumberField


class Profile(models.Model):

    user = models.ForeignKey(User, unique=True)
    mugshot = models.FileField(_('mugshot'), upload_to='mugshots', blank=True)
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


class Link(models.Model):
    """Service type model"""
    profile = models.ForeignKey(Profile)
    title = models.CharField(_('title'), max_length=100)
    url = models.URLField(_('url'), verify_exists=True)

    class Meta:
        verbose_name = _('link')
        verbose_name_plural = _('links')
        db_table = 'user_links'

    def __unicode__(self):
        return u"%s" % self.title