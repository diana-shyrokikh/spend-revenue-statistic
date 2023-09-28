"""
URL configuration for statistic_service project.
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView
)

from revenue.views import RevenueViewSet
from spend.views import SpendViewSet

router = routers.DefaultRouter()
router.register("spend", SpendViewSet)
router.register("revenue", RevenueViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),

    path(
        "api/v1/doc/",
        SpectacularAPIView.as_view(),
        name="schema"
    ),
    path(
        "api/v1/doc/swagger/",
        SpectacularSwaggerView.as_view(
            url_name="schema"
        ),
        name="swagger-ui"
    ),
    path(
        "api/v1/doc/redoc/",
        SpectacularRedocView.as_view(
            url_name="schema"
        ),
        name="redoc"
    ),

    path("api/v1/", include(router.urls)),

    path("api/v1/revenue-statistic/", include(
        "revenue.urls", namespace="revenue_app"
    )),
    path("api/v1/spend-statistic/", include(
        "spend.urls", namespace="spend_app"
    )),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
