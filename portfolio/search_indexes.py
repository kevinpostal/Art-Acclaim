import datetime
from haystack.indexes import *
from haystack import site
from portfolio.models import Portfolio

class PortfolioIndex(SearchIndex):
    text = CharField(document=True, use_template=True)
    title = CharField(model_attr='title') 
    image = CharField(model_attr='image')
    add_date = DateTimeField(model_attr='add_date')

    def get_queryset(self):
        """Used when the entire index for model is updated."""
        return Portfolio.objects.filter(add_date__lte=datetime.datetime.now())


site.register(Portfolio, PortfolioIndex)
