from django import forms
from django.forms import ModelForm, Textarea,FileInput
from django.forms.models import inlineformset_factory
from django.contrib.auth.models import User
from profiles.models import *


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)
        widgets = {
            'first_name': Textarea(attrs={'class': 'edit_input_01'}),      
            'location': Textarea(attrs={'class': 'edit_input_01'}),              
            'quote': Textarea(attrs={'class': 'edit_input_02' }),         
            'education': Textarea(attrs={'class': 'edit_input_03'}),            
            'bio': Textarea(attrs={'class': 'edit_input_04'}),
            'mugshot': FileInput(attrs={'class':'choose_file_button' , 'onchange': "$('.profile_form').eq(0).submit()" }),
        }

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')
        widgets = {
            'first_name': Textarea(attrs={'class': 'edit_input_05'}),      
            'last_name': Textarea(attrs={'class': 'edit_input_05'}),              
        }