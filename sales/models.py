from django.db import models
from datetime import date, timedelta


class WeekDays(object):
    Monday = 0
    Tuesday = 1
    Wednesday = 2
    Thursday = 3
    Friday = 4
    Saturday = 5
    Sunday = 6


class CreditCardNetwork(models.Model):
    network = models.CharField(max_length=64)


class OrdersManager(models.Manager):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)
        self.holidays = None

    def create(
        self,
        credit_card_network: CreditCardNetwork,
        sale_amount: float,
        num_payments: int,
        date: date,
    ):
        order = Orders(
            credit_card_network=credit_card_network,
            sale_amount=sale_amount,
            num_payments=num_payments,
            date=date,
        )
        order.save()

        payment_amount = order.sale_amount / order.num_payments
        for payment in range(order.num_payments):
            payment_date = self.get_payment_date(order.date, payment)
            payment = Payments(
                order=order, amount=payment_amount, truncated=False, date=payment_date
            )
            payment.save()

        return order

    def get_payment_date(self, base_date: date, payment: int) -> date:
        payment_date = base_date + timedelta(days=30 * (payment + 1))
        while self.is_weekend(date) or self.is_bank_holiday(date):
            payment_date = payment_date + timedelta(days=1)
        return payment_date

    def is_weekend(self, date: date) -> bool:
        return date.weekday() in [WeekDays.Sunday, WeekDays.Saturday]

    def is_bank_holiday(self, date: date) -> bool:
        return BankingHolidays.objects.is_holiday(date)


class Orders(models.Model):
    credit_card_network = models.ForeignKey(CreditCardNetwork, on_delete=models.CASCADE)
    sale_amount = models.FloatField()
    num_payments = models.IntegerField()
    date = models.DateField()
    objects = OrdersManager()


class Payments(models.Model):
    order = models.ForeignKey(Orders, related_name="payments", on_delete=models.CASCADE)
    amount = models.FloatField()
    truncated = models.BooleanField()
    date = models.DateField()


class BankingHolidaysManager(models.Manager):
    def is_holiday(self, date: date) -> bool:
        return bool(self.get_queryset().filter(date=date))


class BankingHolidays(models.Model):
    date = models.DateField()
    holiday = models.CharField(max_length=64)
    objects = BankingHolidaysManager()
