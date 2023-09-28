from rest_framework import serializers

from spend.models import SpendStatistic


class SpendSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpendStatistic
        fields = "__all__"


class SpendStatisticSerializer(serializers.ModelSerializer):
    total_revenue = serializers.DecimalField(
        max_digits=10, decimal_places=2, read_only=True
    )

    class Meta:
        model = SpendStatistic
        fields = [
            "name",
            "date",
            "spend",
            "impressions",
            "clicks",
            "conversion",
            "total_revenue",
        ]
