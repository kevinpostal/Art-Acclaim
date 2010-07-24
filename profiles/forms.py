from django import forms
from django.forms import ModelForm, Textarea
from django.forms.models import inlineformset_factory
from django.contrib.auth.models import User
from profiles.models import *


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)
        widgets = {
            'quote': Textarea(attrs={'class': 'edit_input_02' }),
            'education': Textarea(attrs={'class': 'edit_input_03'}),            
            'bio': Textarea(attrs={'class': 'edit_input_04'}),
        }


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')
