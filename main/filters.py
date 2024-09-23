import django_filters
from .models import Evaluation, Aspect

class AspectFilter(django_filters.FilterSet):
    class Meta:
        model = Aspect
        fields = {
            'name': ['icontains'],
        }
