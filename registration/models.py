import datetime
import random
import re

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db import transaction
from django.template.loader import render_to_string
from django.utils.hashcompat import sha_constructor
from django.utils.translation import ugettext_lazy as _
from profiles.models import Profile

SHA1_RE = re.compile('^[a-f0-9]{40}$')


class RegistrationManager(models.Manager):

    def activate_user(self, activation_key):

        # Make sure the key we're trying conforms to the pattern of a
        # SHA1 hash; if it doesn't, no point trying to look it up in
        # the database.
        if SHA1_RE.search(activation_key):
            try:
                account = self.get(activation_key=activation_key)
            except self.model.DoesNotExist:
                return False
            if not account.activation_key_expired():
                user = account.user
                user.is_active = True
                user.save()
                account.activation_key = self.model.ACTIVATED
                account.save()

                Profile(user=user).save()
                return user
        return False
    
    def create_inactive_user(self, username, email, password, site, send_email=True):
        new_user = User.objects.create_user(username, email , password)
        new_user.is_active = False
        new_user.save()

        registration_profile = self.create_profile(new_user)

        if send_email:
            registration_profile.send_activation_email(site)

        return new_user
    create_inactive_user = transaction.commit_on_success(create_inactive_user)

    def create_profile(self, user):

        salt = sha_constructor(str(random.random())).hexdigest()[:5]
        username = user.username
        if isinstance(username, unicode):
            username = username.encode('utf-8')
        activation_key = sha_constructor(salt+username).hexdigest()
        return self.create(user=user,
                           activation_key=activation_key)
        
    def delete_expired_users(self):

        for profile in self.all():
            if profile.activation_key_expired():
                user = profile.user
                if not user.is_active:
                    user.delete()


class RegistrationProfile(models.Model):

    ACTIVATED = u"ALREADY_ACTIVATED"
    
    user = models.ForeignKey(User, unique=True, verbose_name=_('user'))
    activation_key = models.CharField(_('activation key'), max_length=40)
    
    objects = RegistrationManager()
    
    class Meta:
        verbose_name = _('registration profile')
        verbose_name_plural = _('registration profiles')
    
    def __unicode__(self):
        return u"Registration information for %s" % self.user
    
    def activation_key_expired(self):

        expiration_date = datetime.timedelta(days=settings.ACCOUNT_ACTIVATION_DAYS)
        return self.activation_key == self.ACTIVATED or \
               (self.user.date_joined + expiration_date <= datetime.datetime.now())
    activation_key_expired.boolean = True

    def send_activation_email(self, site):

        ctx_dict = {'activation_key': self.activation_key,
                    'expiration_days': settings.ACCOUNT_ACTIVATION_DAYS,
                    'site': site}
        subject = render_to_string('registration/activation_email_subject.txt',
                                   ctx_dict)
        # Email subject *must not* contain newlines
        subject = ''.join(subject.splitlines())
        
        message = render_to_string('registration/activation_email.txt',
                                   ctx_dict)
        
        self.user.email_user(subject, message, settings.DEFAULT_FROM_EMAIL)
    
