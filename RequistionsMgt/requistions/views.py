from django.shortcuts import render,redirect, get_object_or_404
from .models import requistion,requistion_total
from  django.db.models import Sum
from .forms import RequistionForm,RequistiondetailForm

# Create your views here.
def index (request):
    return render(request,'requistions/index.html')

def requistion_list(request):
    ## show all requistions
    #totals=requistion_total.objects.raw("SELECT id, date_made, purpose,made_by_id,(select  sum(rd.amount)from requistions_requistiondetail as rd  where rd.requistionid_id=r.id) as Total from requistions_requistion as r")
    requistions =requistion_total.objects.all().order_by('date_made')    
    context={'requistions': requistions}
    return render(request,'requistions/requistions.html',context)


def requistion_get(request,pk):
    myrequistion=requistion.objects.get(id=pk)
    mydetails=myrequistion.requistiondetail_set.order_by('id')
    context={'requistion':myrequistion,'details':mydetails}
    return render(request,'requistions/requistion.html',context)

def new_requistion(request):
    if request.method !='POST':
        # if no data submitted ,create a blank form
        form=RequistionForm()
    else:
        # post data submitted
        form=RequistionForm(data=request.POST)  
        if form.is_valid():
            form.save()  
            return  redirect('requistions:requistion_list')
        
    #display a blank or invalid form
    context={'form': form}
    return render(request,'requistions/requistion_add.html',context)

    
def add_details(request,requistion_id):
    requistion_instance =  get_object_or_404(requistion, pk=requistion_id)
    form=RequistiondetailForm()
    if request.method =='POST':
        form=RequistiondetailForm(data=request.POST)  
        if form.is_valid():
            detail = form.save(commit=False)
            detail.requistion=requistion_instance
            detail.save()        
            return  redirect(f'requistions/{detail.pk}')
        
    #display a blank or invalid form
    context={'requistion':requistion_instance, 'form': form}
    return render(request,'requistions/requistion_detail_add.html',context)