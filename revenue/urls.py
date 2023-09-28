from django.urls import path

from revenue.views import RevenueStatisticView

app_name = "revenue_app"

urlpatterns = [
    path("", RevenueStatisticView.as_view())
]
