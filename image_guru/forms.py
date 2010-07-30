from django import forms
from django.forms import ModelForm,FileInput
from image_guru.models import *


class Image_Upload_Form(ModelForm):
    class Meta:
        model = Image_Tank
        exclude = ('user','creation_date','hash')
        widgets = {
            'image': FileInput(attrs={'class':'choose_file_button' , 'onchange': "$('.profile_form').eq(0).submit();$(this).attr('disabled','true');" }),
      }
      
    def save(self,user_request):
        from django.core.files.uploadedfile import SimpleUploadedFile
        from cStringIO import StringIO
        from PIL import Image, ImageOps
        
        import hashlib
        import random

        hash = hashlib.sha224(random.random().__str__()).hexdigest()
        
        #Holds Image object
        imgFile = Image.open(self.cleaned_data['image'])
        
        #filename with extension and lowercased
        file_name = self.cleaned_data['image'].name[:-3].lower() + 'png'
        
        #convert to RGB
        if imgFile.mode not in ('L', 'RGB'):  
            imgFile.convert('RGB')
            
        #Size Info
        src_width, src_height = imgFile.size
        src_ratio = float(src_width) / float(src_height)
        dst_width, dst_height = 325, 325
        dst_ratio = float(dst_width) / float(dst_height)
		
        if dst_ratio < src_ratio:
			crop_height = src_height
			crop_width = crop_height * dst_ratio
			x_offset = float(src_width - crop_width) / 2
			y_offset = 0
        else:
			crop_width = src_width
			crop_height = crop_width / dst_ratio
			x_offset = 0
			y_offset = float(src_height - crop_height) / 3
        
        imgFile.thumbnail((650,650), Image.ANTIALIAS)
        #imgFile = imgFile.crop(( x_offset, y_offset, x_offset+int(crop_width), y_offset+int(crop_height) ))
        imgFile = imgFile.resize((dst_width, dst_height), Image.ANTIALIAS)
        #imgFile = ImageOps.fit(imgFile, (325, 325), Image.ANTIALIAS)

        temp_handle = StringIO()
        imgFile.save(temp_handle, 'png')
        temp_handle.seek(0) # Seeks to the start of the image 
        suf = SimpleUploadedFile(file_name,temp_handle.read(), content_type='image/png')
        

        image = Image_Tank(image=suf,user=user_request,hash=hash,type=self.cleaned_data['type'].__str__())
       
        # Remove all image models of that type before saving
        Image_Tank.objects.filter(user=user_request,type=self.cleaned_data['type'].__str__()).delete()
        
        image.save()

        return image
