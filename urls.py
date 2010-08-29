from django.conf.urls.defaults import *
from main_site.views import index_view
from image_guru.views import image_render
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    (r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('registration.urls')),
    (r'^profile/', include('profiles.urls')),
    (r'^portfolio/', include('portfolio.urls')),
    
    (r'^guru/', image_render),   
    # MAIN INDEX
    (r'^$', index_view),   

)

urlpatterns += patterns('django.views.generic.simple',
    (r'about/$', 'direct_to_template', {'template': 'about.html'}),
    (r'privacy/$', 'direct_to_template', {'template': 'privacy.html'}),    
    (r'terms/$', 'direct_to_template', {'template': 'terms.html'}),     
    (r'help/$', 'direct_to_template', {'template': 'help.html'}),         
    )

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '%s/static' % settings.PROJECT_PATH }),
        )
