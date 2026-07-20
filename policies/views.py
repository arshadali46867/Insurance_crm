from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

from datetime import date, timedelta

from .models import Policy
from .serializers import PolicySerializer


class PolicyViewSet(viewsets.ModelViewSet):

    queryset = Policy.objects.all().order_by("-created_at")

    serializer_class = PolicySerializer

    permission_classes = [
        IsAuthenticated
    ]


    @action(
        detail=False,
        methods=['get']
    )
    def renewals(self, request):

        today = date.today()

        upcoming_date = today + timedelta(days=30)


        policies = Policy.objects.filter(
            expiry_date__range=[
                today,
                upcoming_date
            ]
        )


        data = []

        for policy in policies:

            data.append({
                "customer": policy.customer.name,
                "policy_number": policy.policy_number,
                "insurance_type": policy.insurance_type,
                "expiry_date": policy.expiry_date,
                "days_left": (
                    policy.expiry_date - today
                ).days
            })


        return Response(data)