from rest_framework import serializers

class BalanceSerializer(serializers.Serializer):
    balance = serializers.FloatField(min_value=0.0, default=0.0)