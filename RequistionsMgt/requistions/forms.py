from django import forms
from .models import Requisition,RequisitionDetail
class RequisitionForm(forms.ModelForm):
    class Meta:
        model=Requisition
        fields = [
            'made_by',
            'purpose'
        ]


class RequisitionDetailForm(forms.ModelForm):
    class Meta:
        model = RequisitionDetail
        fields = [
            'emp_name',
            'detail_type',
            'period_claimed',
            'ndays',
            'startdate',
            'enddate',
            'rate',
            'amount'
        ]