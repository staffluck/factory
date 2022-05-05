from django.urls import path

from .views import TradePointListAPIView

urlpatterns = [
    path("tradepoints/", TradePointListAPIView.as_view(), ),
]
