from django.conf.urls.defaults import *
from main_site.views import index_view
import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    (r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('registration.urls')),
    (r'^profile/', include('profiles.urls')),         
    # MAIN INDEX
    (r'^$', index_view),   

)
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '%s/static' % settings.PROJECT_PATH }),
        )
