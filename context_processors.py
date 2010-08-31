from profiles.models import *
from portfolio.models import*
from django.db.models import Q

def user_context(request):
    mugshot = ''
    portfolio_count = ''
    acclaim_count = int()
    context = {}
    fan_count = list()
    user_id = request.user.id
    
    if request.user.id:
        try:
            mugshot = Profile.objects.get(id=request.user.id).mugshot.url.__str__()
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
    
            for k, v in vote_hold.items():
                acclaim_count = acclaim_count + v['score']
        
        except:
            pass
    
    context['mugshot'] = mugshot
    context['portfolio_count'] = portfolio_count
    context['acclaim_count'] = acclaim_count
    context['fan_count'] = fan_count
    return context
    
