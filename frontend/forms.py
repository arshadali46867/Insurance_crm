from django import forms

from leads.models import Lead


class LeadForm(forms.ModelForm):

    class Meta:

        model = Lead

        fields = [
            "name",
            "mobile",
            "email",
            "status"
        ]

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),

            "mobile": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),

            "email": forms.EmailInput(
                attrs={
                    "class": "form-control"
                }
            ),

            "status": forms.Select(
                attrs={
                    "class": "form-select"
                }
            ),
        }
from customers.models import Customer


class CustomerForm(forms.ModelForm):

    class Meta:

        model = Customer

        fields = [
            "name",
            "email",
            "mobile",
            "address"
        ]

        widgets = {

            "name": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),

            "email": forms.EmailInput(
                attrs={
                    "class": "form-control"
                }
            ),

            "mobile": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),

            "address": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3
                }
            )
        }        


from policies.models import Policy


class PolicyForm(forms.ModelForm):

    class Meta:

        model = Policy

        fields = [
            "customer",
            "policy_number",
            "insurance_type",
            "insurance_company",
            "premium_amount",
            "start_date",
            "expiry_date"
        ]

        widgets = {

            "customer": forms.Select(
                attrs={
                    "class": "form-select"
                }
            ),

            "policy_number": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),

            "insurance_type": forms.Select(
                attrs={
                    "class": "form-select"
                }
            ),

            "insurance_company": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),

            "premium_amount": forms.NumberInput(
                attrs={
                    "class": "form-control"
                }
            ),

            "start_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date"
                }
            ),

            "expiry_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date"
                }
            )
        }        