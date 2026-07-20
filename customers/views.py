from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Customer
from .serializers import CustomerSerializer

from policies.models import Policy


class CustomerViewSet(viewsets.ModelViewSet):

    queryset = Customer.objects.all().order_by("-created_at")

    serializer_class = CustomerSerializer

    permission_classes = [
        IsAuthenticated
    ]


    @action(
        detail=True,
        methods=['get']
    )
    def policies(self, request, pk=None):

        customer = self.get_object()

        policies = Policy.objects.filter(
            customer=customer
        )

        data = []

        for policy in policies:
            data.append({
                "policy_number": policy.policy_number,
                "insurance_type": policy.insurance_type,
                "insurance_company": policy.insurance_company,
                "premium_amount": policy.premium_amount,
                "start_date": policy.start_date,
                "expiry_date": policy.expiry_date
            })


        return Response({
            "customer": customer.name,
            "policies": data
        })