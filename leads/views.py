from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from .models import Lead
from .serializers import LeadSerializer

from customers.models import Customer
from accounts.models import User


class LeadViewSet(viewsets.ModelViewSet):

    queryset = Lead.objects.all()

    serializer_class = LeadSerializer

    permission_classes = [
        IsAuthenticated
    ]

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter
    ]

    filterset_fields = [
        "status"
    ]

    search_fields = [
        "name",
        "mobile",
        "email"
    ]

    def get_queryset(self):

        user = self.request.user

        # Agent sirf apni leads dekhega
        if user.role == "agent":

            return Lead.objects.filter(
                assigned_to=user
            ).order_by("-created_at")

        # Admin aur Manager sab leads dekhenge
        return Lead.objects.all().order_by("-created_at")

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

    @action(
        detail=True,
        methods=['post']
    )
    def assign(self, request, pk=None):

        lead = self.get_object()

        agent_id = request.data.get("agent_id")

        if not agent_id:
            return Response(
                {
                    "error": "agent_id is required"
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            agent = User.objects.get(
                id=agent_id,
                role="agent"
            )

        except User.DoesNotExist:

            return Response(
                {
                    "error": "Agent not found"
                },
                status=status.HTTP_404_NOT_FOUND
            )

        lead.assigned_to = agent
        lead.save()

        return Response({
            "message": "Lead assigned successfully",
            "lead_id": lead.id,
            "agent_id": agent.id,
            "agent": agent.username
        })