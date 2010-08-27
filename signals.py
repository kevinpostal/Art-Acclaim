import django.dispatch

image_uploaded = django.dispatch.Signal(providing_args=["image", "type"])
