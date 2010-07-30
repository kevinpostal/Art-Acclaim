from django.contrib import admin
from image_guru.models import *


class ImageAdmin(admin.ModelAdmin):
    list_display = ('id','image')
admin.site.register(Image_Tank, ImageAdmin)

