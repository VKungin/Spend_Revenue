from rest_framework import generics
from django.db.models import Sum
from .models import RevenueStatistic
from .serializers import RevenueStatisticSerializer


class RevenueStatisticList(generics.ListAPIView):
    serializer_class = RevenueStatisticSerializer

    def get_queryset(self):
        queryset = RevenueStatistic.objects.values("name", "date").annotate(
            total_revenue=Sum("revenue"),
            total_spend=Sum("spend__spend"),
            total_impressions=Sum("spend__impressions"),
            total_clicks=Sum("spend__clicks"),
            total_conversion=Sum("spend__conversion"),
        )
        return queryset
