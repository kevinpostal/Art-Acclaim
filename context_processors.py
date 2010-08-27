from profiles.models import *
from portfolio.models import*

def mugshot(request):
    mugshot = ''
    portfolio_count = ''
    if request.user.id:
        try:
            mugshot = Profile.objects.get(id=request.user.id).mugshot.url.__str__()
            portfolio_count = Portfolio.objects.filter(user=request.user).count().__str__()
        except:
            pass
            
            
    return {'mugshot': mugshot,'portfolio_count':portfolio_count }