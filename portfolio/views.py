from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import Http404, HttpResponseRedirect
from django.views.generic import list_detail
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from portfolio.forms import *
from portfolio.models import *
from profiles.models import *
from image_guru.forms import * 
from image_guru.views import img_move
from django.conf.urls.defaults import handler404, handler500

@login_required
def portfolio_view(request):
    context = {}
    context['portfolio'] = Portfolio.objects.filter(user=request.user)
    return render_to_response('portfolio/portfolio.html', context, context_instance=RequestContext(request))

@login_required
def portfolio_delete(request,portfolio_id):
    Portfolio.objects.filter(id=portfolio_id).delete()
    return HttpResponseRedirect(reverse('portfolio_view'))

@login_required
def portfolio_edit(request,portfolio_id):
    if request.POST:    
        instance = get_object_or_404(Portfolio, id=portfolio_id)
        portfolio_form = PortfolioForm(request.POST, request.FILES, instance=instance)
        profile = Profile.objects.get(user=request.user)
        
        if portfolio_form.is_valid():
            if request.POST['imagehash']:
                image = img_move(request.POST['imagehash'],profile)
            else:
                image =  portfolio_form.cleaned_data['image']

            materials = portfolio_form.cleaned_data['materials']
            title =  portfolio_form.cleaned_data['title']
            dimensions = portfolio_form.cleaned_data['dimensions']
            creation_date = portfolio_form.cleaned_data['creation_date']
            '''
           portfolio = Portfolio(
                user=request.user,
                image=image,
                title=title,
                creation_date=creation_date,
                dimensions=dimensions,
                materials=materials
                )
            portfolio.save()
            '''    
            portfolio_form.save()
            return HttpResponseRedirect(reverse('portfolio_view'))

    instance = get_object_or_404(Portfolio, id=portfolio_id)
    context = {}
    
    try:
        context['portfolio_image'] = Portfolio.objects.get(id=portfolio_id).image.url.__str__()
    except:
        handler500
        
    context['portfolio_form'] = PortfolioForm(instance=instance)
    context['image_tank'] = Image_Upload_Form()
        
    return render_to_response('portfolio/portfolio_edit.html', context, context_instance=RequestContext(request))

@login_required
def portfolio_add(request):
    if request.POST:
        profile = Profile.objects.get(user=request.user)
        portfolio_form = PortfolioForm(request.POST, request.FILES, instance=profile)
        
        if portfolio_form.is_valid() and request.POST['imagehash']:
           
            image = img_move(request.POST['imagehash'],profile)
            materials = portfolio_form.cleaned_data['materials']
            title =  portfolio_form.cleaned_data['title']
            dimensions = portfolio_form.cleaned_data['dimensions']
            creation_date = portfolio_form.cleaned_data['creation_date']
            portfolio = Portfolio(
                user=request.user,
                image=image,
                title=title,
                creation_date=creation_date,
                dimensions=dimensions,
                materials=materials
                )
            portfolio.save()
            return HttpResponseRedirect(reverse('portfolio_view'))
    else:
        portfolio_form = PortfolioForm()
            
    context = {}
    context['portfolio_form'] = portfolio_form
    context['image_tank'] = Image_Upload_Form()

    return render_to_response('portfolio/portfolio_edit.html', context, context_instance=RequestContext(request))
