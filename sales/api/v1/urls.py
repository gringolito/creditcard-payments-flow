from rest_framework import routers
from sales.api.v1.views import (
    CreditCardNetworksViewSet,
    OrdersViewSet,
    PaymentsViewSet,
    BankingHolidaysViewSet,
    ReportPaymentsViewSet,
)

router = routers.DefaultRouter()
router.register(r"banking-holidays", BankingHolidaysViewSet)
router.register(r"credit-card-networks", CreditCardNetworksViewSet)
router.register(r"orders", OrdersViewSet)
router.register(r"payments", PaymentsViewSet)
router.register(r"report-payments", ReportPaymentsViewSet, basename="report-payments")

urlpatterns = router.urls