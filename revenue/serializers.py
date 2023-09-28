from rest_framework import serializers

from revenue.models import RevenueStatistic


class RevenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = RevenueStatistic
        fields = "__all__"


class RevenueStatisticSerializer(serializers.ModelSerializer):
    total_spend = serializers.DecimalField(
        max_digits=10, decimal_places=2,
        default=0, read_only=True
    )
    total_impressions = serializers.IntegerField(
        default=0, read_only=True
    )
    total_clicks = serializers.IntegerField(
        default=0, read_only=True
    )
    total_conversion = serializers.IntegerField(
        default=0, read_only=True
    )

    class Meta:
        model = RevenueStatistic
        fields = [
            "name",
            "date",
            "revenue",
            "total_spend",
            "total_impressions",
            "total_clicks",
            "total_conversion",
        ]
