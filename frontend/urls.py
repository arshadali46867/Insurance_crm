from django.urls import path

from .views import dashboard
from .views import lead_list
from .views import create_lead
from .views import edit_lead
from .views import delete_lead
from .views import (
    customer_list,
    create_customer,
    edit_customer,
    delete_customer
)
from .views import (
    policy_list,
    create_policy,
    edit_policy,
    delete_policy,
    policy_detail,
    customer_detail,
    lead_detail,
    add_lead_note,
)

urlpatterns = [

    path(
        '',
        dashboard,
        name='dashboard'
    ),

    path(
        'leads/',
        lead_list,
        name='lead_list'
    ),
    path(
    'leads/create/',
    create_lead,
    name='create_lead'
    ),
    path(
    'leads/<int:pk>/edit/',
    edit_lead,
    name='edit_lead'
),

    path(
        'leads/<int:pk>/delete/',
        delete_lead,
        name='delete_lead'
    ),
    path(
    'customers/',
    customer_list,
    name='customer_list'
    ),

    path(
        'customers/create/',
        create_customer,
        name='create_customer'
    ),

    path(
        'customers/<int:pk>/edit/',
        edit_customer,
        name='edit_customer'
    ),

    path(
        'customers/<int:pk>/delete/',
        delete_customer,
        name='delete_customer'
    ),
    path(
    'policies/',
    policy_list,
    name='policy_list'
    ),

    path(
        'policies/create/',
        create_policy,
        name='create_policy'
    ),

    path(
        'policies/<int:pk>/edit/',
        edit_policy,
        name='edit_policy'
    ),

    path(
        'policies/<int:pk>/delete/',
        delete_policy,
        name='delete_policy'
    ),
    path(
    "policies/<int:pk>/",
    policy_detail,
    name="policy_detail"
    ),
    path(
    "customers/<int:pk>/",
    customer_detail,
    name="customer_detail"
),
path(
    "leads/<int:pk>/",
    lead_detail,
    name="lead_detail"
),
path(
    "leads/<int:pk>/add-note/",
    add_lead_note,
    name="add_lead_note"
),

]