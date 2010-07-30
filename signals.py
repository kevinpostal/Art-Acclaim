from django.dispatch import Signal

image_uploaded = Signal(providing_args=["image", "type"])
