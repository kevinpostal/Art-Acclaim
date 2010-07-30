from profiles.models import *

def mugshot(request):
    mugshot = ''
    
    if request.user.id:
        try:
            mugshot = Profile.objects.get(id=request.user.id).mugshot.url.__str__()
        except:
            pass
    return {'mugshot': mugshot }