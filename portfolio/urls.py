from django.conf.urls.defaults import *
from portfolio.views import *


urlpatterns = patterns('',

url(r'add/$',portfolio_add,name='portfolio_add'),
#url(r'^(?P<user_id>[-\d]+)/$',profile_view,name='profile_detail'),
url(r'^$',portfolio_view,name='portfolio_view'),

)
