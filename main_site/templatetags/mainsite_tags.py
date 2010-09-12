from django.template import Library,Variable, Node,TemplateSyntaxError
from profiles.models import Profile
from portfolio.models import *

register = Library()

    
class MugShotNode(Node):
    def __init__(self, user_id):
        self.user_id = Variable(user_id)
    
    def render(self, context):
        user_id = self.user_id.resolve(context)
        try:
            mugshot = Profile.objects.get(user=user_id).mugshot.url_190x190.__str__() #url_190x190 = 190 x 190 image
        except:
            mugshot = ""
        context['mug_shot'] = mugshot
        return ''
    
def get_mugshot(parser, token):
    bits = token.contents.split()

    if len(bits) != 2:
        raise TemplateSyntaxError, "get_mugshot tag takes exactly one argument"
    return MugShotNode(bits[1])
    
get_mugshot = register.tag(get_mugshot)

#############################################################

@register.simple_tag
def get_location(user_id):
    location = Profile.objects.only("location").get(user=user_id).location.__str__()
    return location

##
@register.simple_tag
def get_profile_id(user_id):
    profile_id = Profile.objects.only("id").get(user=user_id).id.__str__()
    return profile_id


##



@register.filter
def truncate(value, arg):
    """
    Truncates a string after a given number of chars  
    Argument: Number of chars to truncate after
    """
    try:
        length = int(arg)
    except ValueError: # invalid literal for int()
        return value # Fail silently.
    if not isinstance(value, basestring):
        value = str(value)
    if (len(value) > length):
        return value[:length] + "..."
    else:
        return value

######################################################################

class AcclaimNode(Node):
    def __init__(self, user_id):
        self.user_id = Variable(user_id)
    
    def render(self, context):
        user_id = self.user_id.resolve(context)
        user_portfolio = Portfolio.objects.filter(user=user_id)
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
            
        context['fan_count'] = fan_count
        context['acclaim_count'] = acclaim_count
        
        return ''
    
def get_acclaim(parser, token):
    bits = token.contents.split()

    if len(bits) != 2:
        raise TemplateSyntaxError, "get_mugshot tag takes exactly one argument"
    return AcclaimNode(bits[1])
    
get_acclaim = register.tag(get_acclaim)



