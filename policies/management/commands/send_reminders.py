from django.core.management.base import BaseCommand
from policies.utils import send_renewal_reminders

class Command(BaseCommand):
    help = "Send policy renewal reminder emails"

    def handle(self, *args, **kwargs):
        send_renewal_reminders()
        self.stdout.write(
            self.style.SUCCESS(
                "Reminder emails sent successfully."
            )
        )