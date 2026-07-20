from django.db import models

# Create your models here.

from customers.models import Customer


class Policy(models.Model):

    INSURANCE_TYPE = (
        ('health', 'Health Insurance'),
        ('motor', 'Motor Insurance'),
        ('life', 'Life Insurance'),
        ('travel', 'Travel Insurance'),
    )


    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name="policies"
    )

    policy_number = models.CharField(
        max_length=50,
        unique=True
    )

    insurance_type = models.CharField(
        max_length=20,
        choices=INSURANCE_TYPE
    )

    insurance_company = models.CharField(
        max_length=100
    )

    premium_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    start_date = models.DateField()

    expiry_date = models.DateField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):
        return self.policy_number