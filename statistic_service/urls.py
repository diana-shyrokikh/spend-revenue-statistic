"""
URL configuration for statistic_service project.
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from revenue.views import RevenueViewSet
from spend.views import SpendViewSet

router = routers.DefaultRouter()
router.register("spend", SpendViewSet)
router.register("revenue", RevenueViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/", include(router.urls)),

    path("api/v1/revenue-statistic/", include(
        "revenue.urls", namespace="revenue_app"
    )),
    path("api/v1/spend-statistic/", include(
        "spend.urls", namespace="spend_app"
    )),
]
