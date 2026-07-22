from django.urls import path

from rest_framework.routers import DefaultRouter

from .views import (PolicyViewSet,export_policies_excel)
from .views import (
    PolicyViewSet,
    export_policies_excel,
    export_policies_pdf
)

router = DefaultRouter()

router.register(
"policies",
PolicyViewSet,
basename="policies")

urlpatterns = [


path(
    "policies/export/",
    export_policies_excel,
    name="export_policies_excel"
),
path(
    "policies/pdf/",
    export_policies_pdf,
    name="export_policies_pdf"
),


]

urlpatterns += router.urls
