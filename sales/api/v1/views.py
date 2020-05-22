from datetime import datetime
from rest_framework import viewsets, permissions, mixins
from rest_framework.response import Response
from sales.models import CreditCardNetwork, Orders, Payments, BankingHolidays
from sales.api.v1.serializers import (
    CreditCardNetworkSerializer,
    OrdersSerializer,
    PaymentsSerializer,
    BankingHolidaysSerializer,
    ReportPaymentsSerializer,
)


class CreditCardNetworksViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Credit Card Networks to be viewed or edited.
    """

    queryset = CreditCardNetwork.objects.all()
    serializer_class = CreditCardNetworkSerializer
    permission_classes = [permissions.IsAdminUser]


class OrdersViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Orders to be viewed or edited.
    """

    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
    permission_classes = [permissions.IsAuthenticated]


class PaymentsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows Orders to be viewed.
    """

    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    permission_classes = [permissions.IsAuthenticated]


class BankingHolidaysViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows BankingHolidays to be viewed or edited.
    """

    queryset = BankingHolidays.objects.all()
    serializer_class = BankingHolidaysSerializer
    permission_classes = [permissions.IsAdminUser]
