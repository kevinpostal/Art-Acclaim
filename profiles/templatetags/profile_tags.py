from django.template import Library,Variable, Node,TemplateSyntaxError
from profiles.models import Profile

register = Library()

    
class MugShotNode(Node):
    def __init__(self, user_id):
        self.user_id = Variable(user_id)
    
    def render(self, context):
        user_id = self.user_id.resolve(context)
        try:
            mugshot = Profile.objects.get(id=user_id).mugshot.url_190x190.__str__() #url_190x190 = 190 x 190 image
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
