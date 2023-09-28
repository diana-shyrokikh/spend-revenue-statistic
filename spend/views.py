from django.db.models import Subquery, OuterRef, Sum
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from revenue.models import RevenueStatistic
from spend.models import SpendStatistic
from spend.serializers import (
    SpendSerializer,
    SpendStatisticSerializer
)


class SpendViewSet(viewsets.ModelViewSet):
    queryset = SpendStatistic.objects.all()
    serializer_class = SpendSerializer


class SpendStaticView(APIView):
    @staticmethod
    def get(request):
        spend_statistic = SpendStatistic.objects.annotate(
            total_revenue=Subquery(
                RevenueStatistic.objects.filter(
                    name=OuterRef("name"), date=OuterRef("date")
                )
                .values("name", "date")
                .annotate(total=Sum("revenue"))
                .values("total")[:1]
            )
        ).values(
            "name",
            "date",
            "spend",
            "impressions",
            "clicks",
            "conversion",
            "total_revenue",
        )

        serializer = SpendStatisticSerializer(
            spend_statistic, many=True
        )

        return Response(
            serializer.data, status=status.HTTP_200_OK
        )
