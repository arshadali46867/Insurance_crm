from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Lead
from .serializers import LeadSerializer

from customers.models import Customer


class LeadViewSet(viewsets.ModelViewSet):

    queryset = Lead.objects.all().order_by("-created_at")

    serializer_class = LeadSerializer

    permission_classes = [
        IsAuthenticated
    ]


    def perform_create(self, serializer):

        serializer.save(
            created_by=self.request.user
        )


    @action(
        detail=True,
        methods=['post']
    )
    def convert(self, request, pk=None):

        lead = self.get_object()

        customer, created = Customer.objects.get_or_create(
                email=lead.email,
                defaults={
                    "name": lead.name,
                    "mobile": lead.mobile
                }
            )

        lead.status = "converted"
        lead.save()


        return Response({
            "message": "Lead converted successfully",
            "customer_id": customer.id,
            "customer_name": customer.name
        })