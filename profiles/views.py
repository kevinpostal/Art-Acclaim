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
from portfolio.models import *

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
            user = User.objects.get(profile=user_id)
        except User.DoesNotExist:
            raise Http404
            
        profile = Profile.objects.get(id=user_id)
        user_portfolio = Portfolio.objects.filter(user=user_id)
        context = {}

        vote_hold =  Vote.objects.get_scores_in_bulk(user_portfolio)
        acclaim_count = int()
        
        #Grabs Fan Count
        fan_count = list()
        for k in user_portfolio.values() :
                fan_count.append( k['id'] )
                
        fan_total = list( Vote.objects.filter(object_id__in=fan_count ).values() )
        fan_count = list() #clear list

        for k in fan_total:
            if k['user_id'].__int__() != int( user_id ):
                fan_count.append( k['user_id'] )
                
        fan_count = len( list(set(fan_count)) ) #Removes duplicates and counts the list
        #!Grabs Fan Count!
        
        # need to add the scores of all the objects
        for k, v in vote_hold.items():
            acclaim_count = acclaim_count + v['score']
        
        try:
            context['user_image'] =  profile.mugshot.url.__str__()
        except:
            pass
         
        if request.user.is_authenticated():
            context['user_profile'] = Profile.objects.get(id=request.user.id)      
            context['user'] = user
        
        context['profile'] = profile
        context['portfolio'] = user_portfolio
        context['name'] = profile.user.get_full_name()
        context['profile_fan_count'] = fan_count
        context['profile_vote_count'] = acclaim_count
        
        return render_to_response('profiles/friend_profile.html', context, context_instance=RequestContext(request))
    else:
        #Only allow logged in users#
        if not request.user.is_authenticated():
            return HttpResponseRedirect(reverse('registration_register')) 
            
        context = {}
        context['profile'] = Profile.objects.get(user=request.user)
        context['user'] = User.objects.get(username=request.user)
        context['name'] = context['user'].get_full_name()
        
        return render_to_response('profiles/profile.html', context, context_instance=RequestContext(request))

@login_required
def profile_edit(request, template_name='profiles/profile_edit.html'):
    """Edit profile."""

    if request.POST:
        profile = Profile.objects.get(user=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        user_form = UserForm(request.POST, instance=request.user)
        
        if profile_form.is_valid() and user_form.is_valid():
            profile_form.save()
            user_form.save()
            
            if request.POST['imagehash']:
                profile.mugshot  = img_move(request.POST['imagehash'],profile)
                profile.save()
            
            return HttpResponseRedirect(reverse('profile_view'))
        else:
            context = {
                'profile_form': profile_form,
                'user_form': user_form,
            }
    else:
        profile = Profile.objects.get(user=request.user)

        context = {
            'profile_form': ProfileForm(instance=profile),
            'image_tank': Image_Upload_Form(),            
            'user_form': UserForm(instance=request.user),
        }
    return render_to_response(template_name, context, context_instance=RequestContext(request))
