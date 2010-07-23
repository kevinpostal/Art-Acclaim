from django.conf.urls.defaults import *
from profiles.views import profile_edit,profile_detail,profile_list


urlpatterns = patterns('',

url(r'edit/$',profile_edit,name='profile_edit'),
url(r'^(?P<username>[-\w]+)/$',profile_detail,name='profile_detail'),
url(r'^$',profile_list,name='profile_list'),

)
