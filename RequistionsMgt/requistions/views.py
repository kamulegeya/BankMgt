from django.shortcuts import render,redirect
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
    myrequistion=requistion.objects.get(id=requistion_id)
    if request.method !='POST':
        # if no data submitted ,create a blank form
        form=RequistiondetailForm()
    else:
        # post data submitted
        form=RequistiondetailForm(data=request.POST)  
        if form.is_valid():
            details=form.save(commit=False)
            #print(myrequistion.pk)
            details.requistion=myrequistion
            print(type(myrequistion))
            details.save()             
            return  redirect('requistions:requistion_get',pk=requistion_id)
        
    #display a blank or invalid form
    context={'requistion':myrequistion,'form': form}
    return render(request,'requistions/requistion_detail_add.html',context)