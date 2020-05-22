from rest_framework import serializers
from sales.models import CreditCardNetwork, Orders, Payments, BankingHolidays


class CreditCardNetworkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CreditCardNetwork
        fields = "__all__"


class OrdersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Orders
        fields = "__all__"
        depth = 1

    class RelatedPaymentsSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
            model = Payments
            fields = ["url", "amount", "truncated", "date"]

    credit_card_network_id = serializers.PrimaryKeyRelatedField(
        queryset=CreditCardNetwork.objects.all(),
        source="credit_card_network",
        write_only=True,
    )
    payments = RelatedPaymentsSerializer(many=True, read_only=True)


class PaymentsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Payments
        fields = "__all__"
        depth = 1


class BankingHolidaysSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BankingHolidays
        fields = "__all__"

