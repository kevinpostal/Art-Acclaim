from settings_local import *
import os
import django

# calculated paths for django and the site
# used as starting points for various other paths
DJANGO_ROOT = os.path.dirname(os.path.realpath(django.__file__))

PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))

COMPRESS_CSS = False



# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Los_Angeles'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PROJECT_PATH, 'static')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/static/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/adminmedia/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '$z8ps0bs=e4s**dz)--o42!#*rsrl=b-n0n)+(!0c*-s9ihq!j'

#Cache System (memcache)
#CACHE_BACKEND = 'memcached://127.0.0.1:11211/'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)


TEMPLATE_CONTEXT_PROCESSORS =  (
        "django.core.context_processors.auth",
        "django.core.context_processors.debug",
        "django.core.context_processors.i18n",
        "django.core.context_processors.media",
        "django.core.context_processors.request",
        'context_processors.user_context',
        
)

INTERNAL_IPS = ('127.0.0.1','10.176.105.169','75.82.209.7')

#CACHE_BACKEND = 'memcached://127.0.0.1:11211/'

INTERNAL_IPS = ('127.0.0.1',)

MIDDLEWARE_CLASSES = (
    'django.middleware.gzip.GZipMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'request.middleware.RequestMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',
    'django.middleware.common.CommonMiddleware',
    'djangodblog.middleware.DBLogMiddleware',
 #   'debug_toolbar.middleware.DebugToolbarMiddleware', #POS will cause errors on vote
)


ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
# Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
# Always use forward slashes, even on Windows.
# Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_PATH, 'layouts'),
)

#Django-Registration
ACCOUNT_ACTIVATION_DAYS = 7 #One-week activation window; you may, of course, use a different value.


# Various apps available
DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.version.VersionDebugPanel',
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.signals.SignalDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
    'debug_toolbar.panels.cache.CacheDebugPanel',

)


DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'EXTRA_SIGNALS': ['signals.image_uploaded'],
    'HIDE_DJANGO_SQL': False,
    'TAG': 'div',
}


AUTH_PROFILE_MODULE = "profiles.Profile"


AUTHENTICATION_BACKENDS = (
    'main_site.views.EmailOrUsernameModelBackend',
    'django.contrib.auth.backends.ModelBackend'
)


INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.humanize',
    'django.contrib.admin',
 #   'debug_toolbar',
 #   'djangodblog',
    'voting',
    'request',
    'registration',
    'profiles',
    'portfolio',
    'image_guru',
#    'devserver', 
#    'django_extensions',

)

#django-devserver

DEVSERVER_MODULES = (
    'devserver.modules.sql.SQLRealTimeModule',
    'devserver.modules.sql.SQLSummaryModule',
    'devserver.modules.profile.ProfileSummaryModule',

    # Modules not enabled by default
    'devserver.modules.ajax.AjaxDumpModule',
    'devserver.modules.profile.MemoryUseModule',
    'devserver.modules.cache.CacheSummaryModule',
    'devserver.modules.request.SessionInfoModule',
)
DEVSERVER_IGNORED_PREFIXES = ['/static']

REQUEST_IGNORE_PATHS = (
        r'^static/(.*)',
        r'^favicon\.ico|favicon\.ico/$',
        r'^__debug__/',
		r'^tinymce/(.*)',
		r'^admin/(.*)',
)



