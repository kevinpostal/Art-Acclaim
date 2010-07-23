from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.http import Http404, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Logging In With Email Addresses in Django                
# http://www.davidcramer.net/code/224/logging-in-with-email-addresses-in-django.html
class EmailOrUsernameModelBackend(object):
    def authenticate(self, username=None, password=None):
        if '@' in username:
            kwargs = {'email': username}
        else:
            kwargs = {'username': username}
        try:
            user = User.objects.get(**kwargs)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None
 
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
##########################################################################


def index_view(request):
    #set up the dictonary
    context = {}

    return render_to_response('index.html',context,context_instance=RequestContext(request))

def auth_view_login(request):
    context = {}
 
    if request.POST:
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                # Redirect to a success page.
                return render_to_response('profiles/profile.html',context,context_instance=RequestContext(request))        
            else:
                # Return a 'disabled account' error message
                return render_to_response('index.html',context,context_instance=RequestContext(request))        
        else:
            # Return an 'invalid login' error message.
            return HttpResponseRedirect(reverse('registration_register'))     
    else:
        return HttpResponseRedirect(reverse('registration_register'))     
