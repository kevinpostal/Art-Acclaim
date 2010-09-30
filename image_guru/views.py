from django.shortcuts import render_to_response
from django.core.files.uploadedfile import SimpleUploadedFile
from django.template import RequestContext
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from image_guru.forms import *
from django.core import serializers

def image_render(request):
        
    if request.POST:
        image_form = Image_Upload_Form(request.POST, request.FILES)

        if request.POST['type']:
            image_form = Image_Upload_Form(request.POST, request.FILES,request.POST['type'].__str__())
            
        if image_form.is_valid():
            image = image_form.save(request.user)
            image = image[0][1] # Grabs the id of the image
            
            return HttpResponse(
                serializers.serialize("json", Image_Tank.objects.filter(id=image), fields=('image','hash')),
                content_type = 'application/javascript; charset=utf8'
            ) 
    return HttpResponse()
    
    
def img_move(hash,profile):
    import shutil 
    
    image_tank = Image_Tank.objects.get(hash=hash)
    img_name = image_tank.image.name.split('/')[1].__str__() # Gets the image name
    # COMMENTING OUT BECUASE OF s3 INTERGRATION
    # AKA Django-Storages
    #
    #img_store =  image_tank.image.path.__str__()
    #image_data = open(img_store, 'rb').read()
    #return SimpleUploadedFile(img_name, image_data)

    return image_tank.image.file
    

