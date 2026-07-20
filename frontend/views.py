from django.shortcuts import render

from leads.models import Lead
from django.shortcuts import render, redirect
from .forms import LeadForm
from django.shortcuts import get_object_or_404

def dashboard(request):

    return render(
        request,
        "dashboard.html"
    )


def lead_list(request):

    leads = Lead.objects.all().order_by(
        "-created_at"
    )

    return render(
        request,
        "leads/list.html",
        {
            "leads": leads
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