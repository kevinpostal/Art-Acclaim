from django.conf.urls.defaults import *
from main_site.views import index_view
from image_guru.views import image_render
from django.conf import settings
from hitcount.views import update_hit_count_ajax
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^ajax/hit/$', update_hit_count_ajax, name='hitcount_update_ajax'),
    (r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('registration.urls')),
    (r'^profile/', include('profiles.urls')),
    (r'^portfolio/', include('portfolio.urls')),
    (r'^gallery/', include('portfolio.gallery_urls')),
    (r'^guru/', image_render),   
    # MAIN INDEX
    (r'^$', index_view),   

)

urlpatterns += patterns('django.views.generic.simple',
    (r'about/$', 'direct_to_template', {'template': 'static/about.html'}),
    (r'privacy/$', 'direct_to_template', {'template': 'static/privacy.html'}),    
    (r'terms/$', 'direct_to_template', {'template': 'static/terms.html'}),     
    (r'help/$', 'direct_to_template', {'template': 'static/help.html'}),         
    )

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '%s/static' % settings.PROJECT_PATH }),
        )
