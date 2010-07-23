from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext



def index_view(request):
    #set up the dictonary
    context = {}


    return render_to_response('index.html',context,context_instance=RequestContext(request))
