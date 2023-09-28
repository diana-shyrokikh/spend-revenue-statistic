from django.urls import path
from spend.views import SpendStatisticView

app_name = "spend_app"

urlpatterns = [
    path("", SpendStatisticView.as_view())
]
