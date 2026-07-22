from django.urls import path

from rest_framework.routers import DefaultRouter

from .views import (
LeadViewSet,
export_leads_excel,export_leads_pdf
)

router = DefaultRouter()

router.register(
"leads",
LeadViewSet,
basename="leads")

urlpatterns = [


path(
    "leads/export/",
    export_leads_excel,
    name="export_leads_excel"
),
path(
    "leads/pdf/",
    export_leads_pdf,
    name="export_leads_pdf"
),


]

urlpatterns += router.urls
