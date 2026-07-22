from django.core.mail import send_mail
from datetime import date

from .models import Policy


def send_renewal_reminders():

    today = date.today()

    policies = Policy.objects.select_related(
        "customer"
    )

    for policy in policies:
        # print(
        #     policy.customer.name,
        #     policy.customer.email,
        #     policy.expiry_date
        #     )
        days_left = (
            policy.expiry_date - today
        ).days

        if days_left in [30, 7]:

            send_mail(
                subject="Policy Renewal Reminder",
                message=(
                    f"Dear {policy.customer.name},\n\n"
                    f"Your policy "
                    f"{policy.policy_number} "
                    f"will expire on "
                    f"{policy.expiry_date}.\n\n"
                    f"Please renew it."
                ),
                from_email=None,
                recipient_list=[
                    policy.customer.email
                ],
                fail_silently=False
            )