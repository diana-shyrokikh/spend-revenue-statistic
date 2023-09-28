from django.db.models import Sum, Subquery, OuterRef
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from revenue.models import RevenueStatistic
from revenue.serializers import (
    RevenueSerializer,
    RevenueStatisticSerializer
)
from spend.models import SpendStatistic


class RevenueViewSet(viewsets.ModelViewSet):
    queryset = RevenueStatistic.objects.all()
    serializer_class = RevenueSerializer


class RevenueStatisticView(APIView):
    @staticmethod
    def get(request):
        revenue_statistic = RevenueStatistic.objects.annotate(
            total_spend=Subquery(
                SpendStatistic.objects.filter(
                    name=OuterRef("name"), date=OuterRef("date")
                )
                .values("name", "date")
                .annotate(total=Sum("spend"))
                .values("total")[:1]
            ),
            total_impressions=Subquery(
                SpendStatistic.objects.filter(
                    name=OuterRef("name"), date=OuterRef("date")
                )
                .values("name", "date")
                .annotate(total=Sum("impressions"))
                .values("total")[:1]
            ),
            total_clicks=Subquery(
                SpendStatistic.objects.filter(
                    name=OuterRef("name"), date=OuterRef("date")
                )
                .values("name", "date")
                .annotate(total=Sum("clicks"))
                .values("total")[:1]
            ),
            total_conversion=Subquery(
                SpendStatistic.objects.filter(
                    name=OuterRef("name"), date=OuterRef("date")
                )
                .values("name", "date")
                .annotate(total=Sum("conversion"))
                .values("total")[:1]
            ),
        ).values(
            "name",
            "date",
            "revenue",
            "total_spend",
            "total_impressions",
            "total_clicks",
            "total_conversion",
        )

        serializer = RevenueStatisticSerializer(
            revenue_statistic, many=True
        )

        return Response(
            serializer.data, status=status.HTTP_200_OK
        )
