from django.urls import path

from .views import dashboard
from .views import lead_list
from .views import create_lead
from .views import edit_lead
from .views import delete_lead

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


]