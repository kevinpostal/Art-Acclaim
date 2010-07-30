from django import forms
from django.forms import ModelForm, Textarea,FileInput
from django.forms.models import inlineformset_factory
from django.contrib.auth.models import User
from portfolio.models import *
class PortfolioForm(ModelForm):
    class Meta:
        model = Art_Work
        exclude = ('user',)
        widgets = {
            'title': Textarea(attrs={'class': 'edit_input_01'}),               
            'materials': Textarea(attrs={'class': 'edit_input_02' }),              
            'creation_date': Textarea(attrs={'class': 'edit_input_05'}),
            'dimensions': Textarea(attrs={'class': 'edit_input_05'}),
            'image': FileInput(attrs={'class':'choose_file_button' , 'onchange': "$('.image_form').eq(0).submit()" }),
        }
        
        
        