from django import forms
from django.forms import ModelForm,FileInput
from image_guru.models import *
from signals import image_uploaded
from image_guru.models import Image_Tank 

class Image_Upload_Form(ModelForm):
    class Meta:
        model = Image_Tank
        exclude = ('user','creation_date','hash')
        widgets = {
            'image': FileInput(attrs={'class':'choose_file_button' , 'onchange': "$('.image_form').eq(0).submit();$(this).attr('disabled','true');" }),
      }
      
    def save(self,user):
        return image_uploaded.send(sender=self,user=user, image=self.cleaned_data['image'], type=self.cleaned_data['type'].__str__() )

         
