from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404, HttpResponseRedirect
from django.views.generic import list_detail
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

@login_required
def portfolio_view(request):
    context = {}
    return render_to_response('portfolio/portfolio.html', context, context_instance=RequestContext(request))

@login_required
def portfolio_add(request):
    context = {}
    return render_to_response('portfolio/portfolio_edit.html', context, context_instance=RequestContext(request))
