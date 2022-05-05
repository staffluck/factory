from rest_framework import serializers


class BaseAuthSerializer(serializers.Serializer):  # Лёгкая замена токенов
    phone = serializers.CharField()


class TradePointOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
