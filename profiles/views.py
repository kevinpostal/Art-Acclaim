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
    if user_id: #Check if request is for your profile or another users
        try:
            user = User.objects.get(profile=user_id)
        except User.DoesNotExist:
            raise Http404
            
        profile = Profile.objects.select_related().get(user=user)

        user_portfolio = Portfolio.objects.select_related().filter(user=user)
        context = {}

        if request.user.is_authenticated():
            context['user_profile'] = Profile.objects.filter(id=request.user.id)      
            context['user'] = user
        
        context['profile'] = profile
        context['portfolio'] = user_portfolio
        context['name'] = profile.user.get_full_name().__str__()
        
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
