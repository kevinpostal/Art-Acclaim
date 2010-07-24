from django.conf.urls.defaults import *
from profiles.views import profile_edit,profile_list,profile_view


urlpatterns = patterns('',

url(r'edit/$',profile_edit,name='profile_edit'),
url(r'^(?P<user_id>[-\d]+)/$',profile_view,name='profile_detail'),
url(r'^$',profile_view,name='profile_view'),

)
