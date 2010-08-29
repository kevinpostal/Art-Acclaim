from django.conf.urls.defaults import *
from portfolio.views import *
from voting.views import xmlhttprequest_vote_on_object
from portfolio.models import Portfolio

widget_dict = {
    'model': Portfolio,
    }


urlpatterns = patterns('',

url(r'add/$',portfolio_add,name='portfolio_add'),
url(r'^(?P<portfolio_id>[\d]+)/edit/$',portfolio_edit,name='portfolio_edit'),
url(r'^(?P<portfolio_id>[\d]+)/delete/$',portfolio_delete,name='portfolio_delete'),
url(r'^vote/(?P<object_id>\w+)/(?P<direction>up|down|clear)/?$', xmlhttprequest_vote_on_object, widget_dict),
url(r'^$',portfolio_view,name='portfolio_view'),

)
