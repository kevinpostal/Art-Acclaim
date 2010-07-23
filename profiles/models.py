import re, datetime
from dateutil import relativedelta

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models import permalink
from django.contrib.auth.models import User
from django.contrib.localflavor.us.models import PhoneNumberField


class Profile(models.Model):
    """Profile model"""
    GENDER_CHOICES = (
        (1, 'Male'),
        (2, 'Female'),
    )
    user = models.ForeignKey(User, unique=True)
    gender = models.PositiveSmallIntegerField(_('gender'), choices=GENDER_CHOICES, blank=True, null=True)
    mugshot = models.FileField(_('mugshot'), upload_to='mugshots', blank=True)
    birth_date = models.DateField(_('birth date'), blank=True, null=True)
    address1 = models.CharField(_('address1'), blank=True, max_length=100)
    address2 = models.CharField(_('address2'), blank=True, max_length=100)
    city = models.CharField(_('city'), blank=True, max_length=100)
    state = models.CharField(_('state'), blank=True, max_length=100, help_text='or Province')
    zip = models.CharField(_('zip'), blank=True, max_length=10)
    country = models.CharField(_('country'), blank=True, max_length=100)
    quote = models.TextField(_('quote'), blank=True)
    
    class Meta:
        verbose_name = _('user profile')
        verbose_name_plural = _('user profiles')
        db_table = 'user_profiles'

    def __unicode__(self):
        return u"%s" % self.user.get_full_name()

    @property
    def age(self):
        TODAY = datetime.date.today()
        if self.birth_date:
            return u"%s" % relativedelta.relativedelta(TODAY, self.birth_date).years
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