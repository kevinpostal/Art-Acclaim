from profiles.models import *
from portfolio.models import*
from django.db.models import Q
from django.contrib.auth.decorators import login_required


@login_required
def user_context(request):
    mugshot = ''
    portfolio_count = ''
    acclaim_count = int()
    context = {}
    fan_count = list()
    user_id = request.user.id

    try:  
        mugshot = Profile.objects.get(user=request.user).mugshot
    except:
        pass   
    
    portfolio = Portfolio.objects.filter(user=request.user)
    portfolio_count = len(portfolio)
    vote_hold =  Vote.objects.get_scores_in_bulk(portfolio)
    
    for k in list ( portfolio.values() ) :
        fan_count.append( k['id'] )

    fan_total = list( Vote.objects.filter(object_id__in=fan_count ).values() )
    fan_count = list() #clear list

    for k in fan_total:
        if k['user_id'].__int__() != user_id:
            fan_count.append( k['user_id'] )
    fan_count = len( list(set(fan_count)) ) #Removes duplicates and counts the list
    # need to add the scores of all the objects
    for k, v in vote_hold.items():
        acclaim_count = acclaim_count + v['score']
        
        #Check for empty list
    if not fan_count:
        fan_count = 0

    context['our_profile']  = Profile.objects.get(user=request.user)
    context['our_mugshot'] = mugshot
    context['our_portfolio_count'] = portfolio_count.__str__()
    context['our_acclaim_count'] = acclaim_count.__str__()
    context['our_fan_count'] = fan_count.__str__()
    return context
    
