from django.db.models.signals import post_delete
from portfolio.models import Portfolio
from voting.models import Vote

import django.dispatch

def del_vote(sender, **kwargs):
    Vote.objects.get(object_id=kwargs['instance'].id).delete()

post_delete.connect(del_vote, sender=Portfolio)

image_uploaded = django.dispatch.Signal(providing_args=["image", "type"])
