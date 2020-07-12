from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

# Create your models here.
class Station(models.Model):
    station_name=models.CharField(max_length=100,verbose_name='station')
    class Meta:
        verbose_name_plural='stations'
    def __str__ (self):
        return self.station_name
class Position(models.Model):
    position_name=models.CharField(max_length=100,verbose_name='position')
    class Meta:
        verbose_name_plural='positions'
    def __str__ (self):
        return self.position_name
class SalaryScale(models.Model):
    scale_name=models.CharField(max_length=100,verbose_name='salary scale name')
    class Meta:
        verbose_name_plural='salaryscales'
    def __str__ (self):
        return self.scale_name

class RequestType(models.Model):
    ## e.g NOA,SDA,Advance
    type_name=models.CharField(max_length=100, verbose_name='Requisition Type')
    class Meta:
        verbose_name_plural='requesttypes'
    def __str__ (self):
        return self.type_name
class RateType(models.Model):
    ## e.g travel abroad, travel inland
    type_name=models.CharField(max_length=100, verbose_name='Rate Type')
    class Meta:
        verbose_name_plural='ratetypes'
    def __str__ (self):
        return self.type_name
## Allowances rates ...depending on rate type and salary scales
class AllowanceRate(models.Model):    
    allowance_scale=models.ForeignKey(SalaryScale,on_delete=models.CASCADE)
    allowance_rate=models.ForeignKey(RateType,on_delete=models.CASCADE)
    amount=models.FloatField(default=0)
    class Meta:
        verbose_name_plural='Allowance rates'
    def __str__ (self):
        return self.allowance_rate

class Directorate(models.Model):
    directorate_name=models.CharField(max_length=100)
    class Meta:
        verbose_name_plural='Directorates'


    def __str__ (self):
        return self.directorate_name
    
class Period(models.Model):
    period_name=models.CharField(max_length=50,verbose_name='Period name')
    p_number=models.IntegerField(verbose_name='period number')
    startdate=models.DateField()
    enddate=models.DateField()
    num_days=models.IntegerField(default=30,verbose_name="Number of Days")
    p_flag=models.BooleanField(default=True)

    class Meta:
        verbose_name_plural='Periods'
    def __str__ (self):
        return self.period_name

class Employee(models.Model):
    emp_name=models.CharField(max_length=200,verbose_name='employee name')
    staff_id_num=models.CharField(max_length=20, unique=True, verbose_name='UNRAID No.')
    emp_station=models.ForeignKey(Station, on_delete=models.CASCADE)
    emp_position=models.ForeignKey(Position, on_delete=models.CASCADE)
    emp_scale=models.ForeignKey(SalaryScale, on_delete=models.CASCADE)
    date_left_org=models.DateField(null=True)
    class Meta:
        verbose_name_plural='Employees'
    def __str__ (self):
        return self.emp_name

class RequisitionDetailType(models.Model):
    ## e.g request for NOA,SDA,Advance,expense claim
    detail_name=models.CharField(max_length=100)
    objects = models.Manager()
    class Meta:
        verbose_name_plural='Requisition detail types'
    def __str__ (self):
        return self.detail_name
class Requisition(models.Model):
    made_by=models.ForeignKey(Employee, on_delete=models.CASCADE)
    date_made=models.DateTimeField(auto_now_add=True)
    purpose=models.TextField(verbose_name='Purpose')
    total =models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    class Meta:
        verbose_name_plural='Requisition'
    def __str__ (self):
        return self.purpose
class RequisitionDetail(models.Model):
    requisition = models.ForeignKey(Requisition, null=True, on_delete=models.CASCADE)
    emp_name = models.ForeignKey(Employee, on_delete=models.CASCADE)
    detail_type = models.ForeignKey(RequisitionDetailType, on_delete=models.CASCADE)
    period_claimed = models.ForeignKey(Period, on_delete=models.CASCADE)
    ndays = models.IntegerField(default=0, verbose_name="Number of days")
    startdate = models.DateField(null=True)
    enddate = models.DateField(null=True)
    rate = models.DecimalField(max_digits=10, decimal_places=2, default=0.0, verbose_name='Allowances Rate')
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0, verbose_name='Amount')
    class Meta:
        verbose_name_plural='Requisition details'
        
@receiver(post_save, sender=RequisitionDetail)
def add_requisition_total(sender, instance, **kwargs):
    requisition = instance.requisition
    requisition.total = requisition.total + instance.amount
    requisition.save()

@receiver(post_delete, sender=RequisitionDetail)
def substract_requisition_total(sender, instance, **kwargs):
    requisition = instance.requisition
    requisition.total = requisition.total - instance.amount
    requisition.save()
class RequisitionTotal(models.Model) :
    date_made=models.DateField(db_column='date_made')
    purpose=models.CharField(max_length=400, db_column='purpose')
    made_by=models.ForeignKey(Employee, on_delete=models.DO_NOTHING)
    total=models.FloatField(db_column='Total')   
    
    def __str__ (self):
        return self.purpose
    class Meta:
        verbose_name_plural='Requisition totals'