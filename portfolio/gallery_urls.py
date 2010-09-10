from django.conf.urls.defaults import *
from portfolio.views import *
from portfolio.models import Portfolio

urlpatterns = patterns('',
url(r'^$',gallery_view,name='gallery_view'),


)
