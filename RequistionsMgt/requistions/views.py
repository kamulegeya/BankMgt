from django.shortcuts import render,redirect, get_object_or_404
from .models import Requisition,RequisitionTotal
from  django.db.models import Sum
from .forms import RequisitionForm, RequisitionDetailForm

# Create your views here.
def index (request):
    return render(request,'requistions/index.html')

def requisition_list(request):
    requisitions = Requisition.objects.all().order_by('date_made') 
    return render(request,'requistions/requistions.html', {
        "requisitions": requisitions
    })


def get_requisition(request,pk):
    requisition = Requisition.objects.get(id=pk)
    req_details = requisition.requisitiondetail_set.order_by('id')
    context={
        'requisition': requisition, 
        'details':req_details
    }
    return render(request,'requistions/requistion.html',context)

def new_requistion(request):
    if request.method !='POST':
        # if no data submitted ,create a blank form
        form=RequisitionForm()
    else:
        # post data submitted
        form=RequistionForm(data=request.POST)  
        if form.is_valid():
            form.save()  
            return  redirect('requistions:requistion_list')
        
    #display a blank or invalid form
    context={'form': form}
    return render(request,'requistions/requistion_add.html',context)

    
def add_details(request, requistion_id):
    requisition =  Requisition.objects.get(pk=requistion_id)
    form = RequisitionDetailForm(request.POST or None)
    if form.is_valid():
        detail = form.save(commit=False)
        detail.requisition = requisition
        detail.save()        
        return  redirect('requistions:requistion_get', pk=requisition.id)
    context = {
        'requistion':requisition,
        'form': form
    }
    return render(request,'requistions/requistion_detail_add.html',context)