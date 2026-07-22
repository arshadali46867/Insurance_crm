from django.urls import path

from rest_framework.routers import DefaultRouter

from .views import (
CustomerViewSet,
export_customers_excel
)
from .views import (
    CustomerViewSet,
    export_customers_excel,
    export_customers_pdf
)

router = DefaultRouter()

router.register(
"customers",
CustomerViewSet,
basename="customers")

urlpatterns = [


path(
    "customers/export/",
    export_customers_excel,
    name="export_customers_excel"
),
path(
    "customers/pdf/",
    export_customers_pdf,
    name="export_customers_pdf"
),


]

urlpatterns += router.urls
