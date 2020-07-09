from django import forms
from .models import requistion,requistiondetail
class RequistionForm(forms.ModelForm):
    class Meta:
        model=requistion
        fields ='__all__'


class RequistiondetailForm(forms.ModelForm):
    class Meta:
        model=requistiondetail
        fields =['emp_name','detail_type','period_claimed','ndays','startdate','enddate','rate','amount']