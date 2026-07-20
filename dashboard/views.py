from datetime import date, timedelta

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from leads.models import Lead
from customers.models import Customer
from policies.models import Policy


class DashboardAPIView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def get(self, request):

        user = request.user

        # Agent Dashboard
        if user.role == "agent":

            total_assigned_leads = Lead.objects.filter(
                assigned_to=user
            ).count()

            converted_leads = Lead.objects.filter(
                assigned_to=user,
                status="converted"
            ).count()

            new_leads = Lead.objects.filter(
                assigned_to=user,
                status="new"
            ).count()

            interested_leads = Lead.objects.filter(
                assigned_to=user,
                status="interested"
            ).count()

            return Response({
                "dashboard_type": "agent",
                "total_assigned_leads": total_assigned_leads,
                "converted_leads": converted_leads,
                "new_leads": new_leads,
                "interested_leads": interested_leads
            })

        # Admin / Manager Dashboard
        total_leads = Lead.objects.count()

        total_customers = Customer.objects.count()

        total_policies = Policy.objects.count()

        today = date.today()

        upcoming_date = today + timedelta(days=30)

        upcoming_renewals = Policy.objects.filter(
            expiry_date__range=[
                today,
                upcoming_date
            ]
        ).count()

        return Response({

            "dashboard_type": "admin",

            "total_leads": total_leads,

            "total_customers": total_customers,

            "total_policies": total_policies,

            "upcoming_renewals": upcoming_renewals

        })