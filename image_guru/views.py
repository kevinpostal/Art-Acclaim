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

            return HttpResponse(
                serializers.serialize("json", Image_Tank.objects.filter(id=image.id), fields=('image','hash')),
                content_type = 'application/javascript; charset=utf8'
            ) 
    return HttpResponse()
    
    
def img_move(hash,profile):
    import shutil 
    
   # import pdb; pdb.set_trace()
    
    image_tank = Image_Tank.objects.get(hash=hash)
    img_store =  image_tank.image.path.__str__()
    img_name =image_tank.image.name.split('/')[1][:-4].__str__()
    image_data = open(img_store, 'rb').read()

    profile.mugshot  = SimpleUploadedFile(img_name, image_data)
    profile.save()
    image_tank.delete()


    
    return