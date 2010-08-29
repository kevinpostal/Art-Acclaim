from django.contrib import admin
from portfolio.models import *

class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    
admin.site.register(Portfolio,PortfolioAdmin)
