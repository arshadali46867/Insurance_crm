from django.shortcuts import render

# Create your views here.
from activity_logs.models import ActivityLog


def perform_create(self, serializer):

    lead = serializer.save(
        created_by=self.request.user
    )

    ActivityLog.objects.create(
        user=self.request.user,
        action=f"Created Lead {lead.name}"
    )