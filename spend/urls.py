from django.urls import path
from spend.views import SpendStaticView

app_name = "spend_app"

urlpatterns = [
    path("", SpendStaticView.as_view())
]
