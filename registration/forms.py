"""
Forms and validation code for user registration.

"""

from django.contrib.auth.models import User
from django import forms
from django.utils.translation import ugettext_lazy as _

#CSS Classes of Forms
attrs_dict = { 'class': 'join_form_text' }


class RegistrationForm(forms.Form):

    first_name = forms.CharField(widget=forms.TextInput(attrs=attrs_dict))
    last_name = forms.CharField(widget=forms.TextInput(attrs=attrs_dict))
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(attrs_dict,maxlength=75)),label=_(u'email address'))

    password = forms.CharField(widget=forms.PasswordInput(attrs=attrs_dict, render_value=False),label=_(u'password'))

    def clean_email(self):
        """
        Validate that the email is not already in use.
        
        """
        try:
            user = User.objects.get(email__iexact=self.cleaned_data['email'])
        except User.DoesNotExist:
            return self.cleaned_data['email']
        raise forms.ValidationError(_("A user with that email already exists."))

    def save(self, profile_callback=None):
        """
        Create the new ``User`` and ``RegistrationProfile``, and
        returns the ``User``.
        
        This is essentially a light wrapper around
        ``RegistrationProfile.objects.create_inactive_user()``,
        feeding it the form data and a profile callback (see the
        documentation on ``create_inactive_user()`` for details) if
        supplied.
        
        """
        


        new_user = RegistrationProfile.objects.create_inactive_user(username=self.cleaned_data['last_name'],
                                                                    password=self.cleaned_data['password'],
                                                                    email=self.cleaned_data['email'],
                                                                    profile_callback=profile_callback)
        import pdb; pdb.set_trace()                                                            
        return new_user
