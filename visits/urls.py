from django.urls import path

from .views import TradePointListAPIView, VisitCreateAPIView

urlpatterns = [
    path("tradepoints/", TradePointListAPIView.as_view(), ),
    path("create_visit/", VisitCreateAPIView.as_view(), )
]
