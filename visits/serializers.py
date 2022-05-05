from rest_framework import serializers

from .models import TradePoint


class BaseAuthSerializer(serializers.Serializer):  # Лёгкая замена токенов
    phone = serializers.CharField()


class TradePointOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()


class VisitInputSerializer(serializers.Serializer):
    tradepoint = serializers.PrimaryKeyRelatedField(queryset=TradePoint.objects.select_related("employee").all())
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()

class VisitOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    created_at = serializers.DateTimeField()
