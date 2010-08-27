from django.conf.urls.defaults import *
from portfolio.views import *


urlpatterns = patterns('',

url(r'add/$',portfolio_add,name='portfolio_add'),
url(r'^(?P<portfolio_id>[\d]+)/edit/$',portfolio_edit,name='portfolio_edit'),
url(r'^(?P<portfolio_id>[\d]+)/delete/$',portfolio_delete,name='portfolio_delete'),

url(r'^$',portfolio_view,name='portfolio_view'),

)
