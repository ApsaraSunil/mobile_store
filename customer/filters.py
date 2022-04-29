import django_filters
from owner.models import Mobiles


class MobileFilter(django_filters.FilterSet):
    class Meta:
        model = Mobiles
        fields = {
            "mobile_name": ["contains"],
            "price":       ["lt", "gt"]
        }
