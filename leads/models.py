from django.db import models
from django.conf import settings


class Lead(models.Model):

    STATUS_CHOICES = (
        ('new', 'New'),
        ('contacted', 'Contacted'),
        ('interested', 'Interested'),
        ('quotation_sent', 'Quotation Sent'),
        ('converted', 'Converted'),
    )

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    assigned_to = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.SET_NULL,
    null=True,
    blank=True,
    related_name="assigned_leads"
) 

    name = models.CharField(max_length=100)

    mobile = models.CharField(
        max_length=15
    )

    email = models.EmailField(
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default='new'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):
        return self.name