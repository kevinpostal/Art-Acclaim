from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.http import Http404, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from portfolio.models import *
from voting.models import Vote
from heapq import nlargest 
from operator import itemgetter 

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

    hold = {}
    acclaim_count = int()
    user_list = User.objects.all()

    for user in user_list:
        user_portfolio = Portfolio.objects.filter(user=user)
        vote_hold =  Vote.objects.get_scores_in_bulk(user_portfolio)
        
        if vote_hold: # make sure we got a list to work with
            acclaim_count = 0 # Reset Acclaim Count
            # need to add the scores of all the objects
            for k, v in vote_hold.items():
                acclaim_count = acclaim_count + v['score']
                
            hold[user] = acclaim_count # Set hold context to key:user value:count

    context['top_artists'] = nlargest(5, hold.iteritems(), itemgetter(1)) #sorts Dictonary by value
    context['top_art'] = Vote.objects.get_top(Portfolio,limit=5)
    context['recent_art'] = Portfolio.objects.order_by('creation_date')[:12]
    
    #context['form'] = AuthenticationForm()

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
                return HttpResponseRedirect(reverse('profile_view')) 
            else:
                # Return a 'disabled account' error message
                return render_to_response('index.html',context,context_instance=RequestContext(request))        
        else:
            # Return an 'invalid login' error message.
            return HttpResponseRedirect(reverse('registration_register'))     
    else:
        return HttpResponseRedirect(reverse('registration_register'))     
