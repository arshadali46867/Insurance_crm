from django.shortcuts import render
from django.db.models import Q

from leads.models import Lead,LeadNote
from django.shortcuts import render, redirect
from .forms import LeadForm
from django.shortcuts import get_object_or_404
from customers.models import Customer
from .forms import CustomerForm
from policies.models import Policy
from .forms import PolicyForm
from datetime import date, timedelta
from leads.models import Lead
from django.core.paginator import Paginator
from django.db.models import Count
from accounts.models import User
from django.contrib.auth.decorators import login_required


def dashboard(request):

    total_leads = Lead.objects.count()

    total_customers = Customer.objects.count()

    total_policies = Policy.objects.count()

    today = date.today()

    renewal_date = today + timedelta(days=30)

    upcoming_renewals = Policy.objects.filter(
        expiry_date__lte=renewal_date,
        expiry_date__gte=today
    ).count()

    recent_leads = Lead.objects.order_by(
        "-created_at"
    )[:5]
    
    agent_performance = User.objects.filter(
    role="agent"
    ).annotate(
        total_leads=Count("assigned_leads")
    ).order_by(
        "-total_leads"
    )
    new_leads = Lead.objects.filter(
    status="new"
    ).count()

    contacted_leads = Lead.objects.filter(
        status="contacted"
    ).count()

    interested_leads = Lead.objects.filter(
        status="interested"
    ).count()

    quotation_sent_leads = Lead.objects.filter(
        status="quotation_sent"
    ).count()

    converted_leads = Lead.objects.filter(
        status="converted"
    ).count()
    upcoming_date = today + timedelta(days=30)
    upcoming_policies = Policy.objects.select_related(
    "customer"
    ).filter(
        expiry_date__gte=today,
        expiry_date__lte=upcoming_date
    ).order_by(
        "expiry_date"
    )[:10]
    top_agent = agent_performance.first()
    return render(
        request,
        "dashboard.html",
        {
            "total_leads": total_leads,
            "total_customers": total_customers,
            "total_policies": total_policies,
            "upcoming_renewals": upcoming_renewals,
            "recent_leads": recent_leads,
            "agent_performance": agent_performance,
            "new_leads": new_leads,
            "contacted_leads": contacted_leads,
            "interested_leads": interested_leads,
            "quotation_sent_leads": quotation_sent_leads,
            "converted_leads": converted_leads,
            "upcoming_policies": upcoming_policies,
            "top_agent": top_agent,
        }
    )




def lead_list(request):

    search = request.GET.get(
        "search",
        ""
    )

    leads = Lead.objects.all()

    if search:

        leads = leads.filter(

            Q(name__icontains=search) |

            Q(mobile__icontains=search) |

            Q(email__icontains=search)

        )

    leads = leads.order_by(
        "-created_at"
    )
    leads = leads.order_by("-created_at")

    paginator = Paginator(leads, 10)

    page_number = request.GET.get("page")

    leads = paginator.get_page(page_number)

    return render(
        request,
        "leads/list.html",
        {
            "leads": leads,
            "search": search
        }
    )
def create_lead(request):

    if request.method == "POST":

        form = LeadForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect(
                "lead_list"
            )

    else:

        form = LeadForm()

    return render(
        request,
        "leads/create.html",
        {
            "form": form
        }
    )


def edit_lead(request, pk):

    lead = get_object_or_404(
        Lead,
        id=pk
    )

    if request.method == "POST":

        form = LeadForm(
            request.POST,
            instance=lead
        )

        if form.is_valid():

            form.save()

            return redirect(
                "lead_list"
            )

    else:

        form = LeadForm(
            instance=lead
        )

    return render(
        request,
        "leads/edit.html",
        {
            "form": form
        }
    )


def delete_lead(request, pk):

    lead = get_object_or_404(
        Lead,
        id=pk
    )

    lead.delete()

    return redirect(
        "lead_list"
    )

def customer_list(request):

    search = request.GET.get(
        "search",
        ""
    )

    customers = Customer.objects.all()

    if search:

        customers = customers.filter(

            Q(name__icontains=search) |

            Q(email__icontains=search) |

            Q(mobile__icontains=search)

        )

    customers = customers.order_by(
        "-created_at"
    )

    return render(
        request,
        "customers/list.html",
        {
            "customers": customers,
            "search": search
        }
    )


def create_customer(request):

    if request.method == "POST":

        form = CustomerForm(
            request.POST
        )

        if form.is_valid():

            form.save()

            return redirect(
                "customer_list"
            )

    else:

        form = CustomerForm()

    return render(
        request,
        "customers/create.html",
        {
            "form": form
        }
    )


def edit_customer(request, pk):

    customer = get_object_or_404(
        Customer,
        id=pk
    )

    if request.method == "POST":

        form = CustomerForm(
            request.POST,
            instance=customer
        )

        if form.is_valid():

            form.save()

            return redirect(
                "customer_list"
            )

    else:

        form = CustomerForm(
            instance=customer
        )

    return render(
        request,
        "customers/edit.html",
        {
            "form": form
        }
    )


def delete_customer(request, pk):

    customer = get_object_or_404(
        Customer,
        id=pk
    )

    customer.delete()

    return redirect(
        "customer_list"
    )





def policy_list(request):

    search = request.GET.get(
        "search",
        ""
    )

    policies = Policy.objects.select_related(
        "customer"
    )

    if search:

        policies = policies.filter(

            Q(policy_number__icontains=search) |

            Q(insurance_company__icontains=search) |

            Q(customer__name__icontains=search)

        )

    policies = policies.order_by(
        "-created_at"
    )

    today = date.today()

    renewal_date = today + timedelta(days=30)

    return render(
        request,
        "policies/list.html",
        {
            "policies": policies,
            "search": search,
            "today": today,
            "renewal_date": renewal_date
        }
    )


def create_policy(request):

    if request.method == "POST":

        form = PolicyForm(
            request.POST
        )

        if form.is_valid():

            form.save()

            return redirect(
                "policy_list"
            )

    else:

        form = PolicyForm()

    return render(
        request,
        "policies/create.html",
        {
            "form": form
        }
    )


def edit_policy(request, pk):

    policy = get_object_or_404(
        Policy,
        id=pk
    )

    if request.method == "POST":

        form = PolicyForm(
            request.POST,
            instance=policy
        )

        if form.is_valid():

            form.save()

            return redirect(
                "policy_list"
            )

    else:

        form = PolicyForm(
            instance=policy
        )

    return render(
        request,
        "policies/edit.html",
        {
            "form": form
        }
    )


def delete_policy(request, pk):

    policy = get_object_or_404(
        Policy,
        id=pk
    )

    policy.delete()

    return redirect(
        "policy_list"
    )


from policies.models import Policy


def policy_detail(request, pk):

    policy = Policy.objects.select_related(
        "customer"
    ).get(id=pk)

    return render(
        request,
        "policies/detail.html",
        {
            "policy": policy
        }
    )

def customer_detail(request, pk):

    customer = Customer.objects.get(
        id=pk
    )

    policies = Policy.objects.filter(
        customer=customer
    )

    return render(
        request,
        "customers/detail.html",
        {
            "customer": customer,
            "policies": policies
        }
    )
def lead_detail(request, pk):

    lead = Lead.objects.select_related(
        "assigned_to",
        "created_by"
    ).get(id=pk)

    notes = LeadNote.objects.filter(
    lead=lead
    ).order_by("-created_at")

    return render(
        request,
        "leads/detail.html",
        {
            "lead": lead,
            "notes": notes,
        }
    )

def add_lead_note(request, pk):

    lead = Lead.objects.get(id=pk)

    if request.method == "POST":

        LeadNote.objects.create(
            lead=lead,
            note=request.POST.get("note"),
            created_by=request.user
        )

    return redirect(
        f"/leads/{pk}/"
    )