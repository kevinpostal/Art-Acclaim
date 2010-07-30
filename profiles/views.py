from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404, HttpResponseRedirect
from django.views.generic import list_detail
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from profiles.models import *
from profiles.forms import *
from image_guru.views import img_move
from image_guru.forms import *

def profile_list(request):
    return list_detail.object_list(
        request,
        queryset=Profile.objects.all(),
        paginate_by=20,
    )
profile_list.__doc__ = list_detail.object_list.__doc__


def profile_view(request, user_id=""):
#Check if request is for your profile or another users
    if user_id:
        try:
            user = User.objects.get(id__iexact=user_id)
        except User.DoesNotExist:
            raise Http404
            
        profile = Profile.objects.get(user=user)
        context = {}
        context['profile'] = profile
       
        try:
            context['user_image'] =  context['profile'].mugshot.url.__str__()
        except:
            pass
         
         
        if request.user.id:
            try:
                context['mugshot'] =  Profile.objects.get(id=request.user.id).mugshot.url.__str__()
            except:
                pass
            
        context['user'] = user
        context['name'] = context['user'].get_full_name()
        
        return render_to_response('profiles/friend_profile.html', context, context_instance=RequestContext(request))
    else:
        #Only allow logged in users#
        if not request.user.is_authenticated():
            return HttpResponseRedirect(reverse('registration_register')) 
            
        context = {}
        context['profile'] = Profile.objects.get(user=request.user)
        context['user'] = User.objects.get(username=request.user)
       
        try:
            context['mugshot'] =  context['profile'].mugshot.url.__str__()
        except:
            pass

        context['name'] = context['user'].get_full_name()
        
        return render_to_response('profiles/profile.html', context, context_instance=RequestContext(request))

@login_required
def profile_edit(request, template_name='profiles/profile_edit.html'):
    """Edit profile."""
    
    mugshot = "" # Create an empty mugshot variable
    
    if request.POST:
        profile = Profile.objects.get(user=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        user_form = UserForm(request.POST, instance=request.user)
        
        try:
            mugshot = profile.mugshot.url.__str__()
        except:
            pass
            
        if profile_form.is_valid() and user_form.is_valid():
            profile_form.save()
            user_form.save()
            
            if request.POST['imagehash']:
                img_move(request.POST['imagehash'],profile)
               
            
            return HttpResponseRedirect(reverse('profile_view'))
        else:
            context = {
                'profile_form': profile_form,
                'user_form': user_form,
                'mugshot': mugshot
            }
    else:
        profile = Profile.objects.get(user=request.user)
        
        try:
            mugshot = profile.mugshot.url.__str__()
        except:
            pass
            
        context = {
            'profile_form': ProfileForm(instance=profile),
            'image_tank': Image_Upload_Form(),            
            'user_form': UserForm(instance=request.user),
            'mugshot': mugshot
        }
    return render_to_response(template_name, context, context_instance=RequestContext(request))
