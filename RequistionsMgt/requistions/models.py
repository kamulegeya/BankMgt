from django.db import models

# Create your models here.
class station(models.Model):
    station_name=models.CharField(max_length=100,verbose_name='station')
    objects = models.Manager()
    class Meta:
        verbose_name_plural='stations'
    def __str__ (self):
        return self.station_name
class position(models.Model):
    position_name=models.CharField(max_length=100,verbose_name='position')
    objects = models.Manager()
    class Meta:
        verbose_name_plural='positions'
    def __str__ (self):
        return self.position_name
class salaryscale(models.Model):
    scale_name=models.CharField(max_length=100,verbose_name='salary scale name')
    objects = models.Manager()
    class Meta:
        verbose_name_plural='salaryscales'
    def __str__ (self):
        return self.scale_name

class requesttype(models.Model):
    ## e.g NOA,SDA,Advance
    type_name=models.CharField(max_length=100,verbose_name='Requistion Type')
    objects = models.Manager()
    class Meta:
        verbose_name_plural='requesttypes'
    def __str__ (self):
        return self.type_name
class ratetype(models.Model):
    ## e.g travel abroad, travel inland
    type_name=models.CharField(max_length=100,verbose_name='Rate Type')
    objects = models.Manager()
    class Meta:
        verbose_name_plural='ratetypes'
    def __str__ (self):
        return self.type_name
## Allowances rates ...depending on rate type and salary scales
class allowancerate(models.Model):    
    allowance_scale=models.ForeignKey(salaryscale,on_delete=models.CASCADE)
    allowance_rate=models.ForeignKey(ratetype,on_delete=models.CASCADE)
    amount=models.FloatField(default=0)
    objects = models.Manager()
    class Meta:
        verbose_name_plural='allowancerates'
    def __str__ (self):
        return self.allowance_rate

class directorate(models.Model):
    directorate_name=models.CharField(max_length=100)
    objects = models.Manager()
    class Meta:
        verbose_name_plural='directorates'


    def __str__ (self):
        return self.directorate_name
    
class period(models.Model):
    period_name=models.CharField(max_length=50,verbose_name='Period name')
    p_number=models.IntegerField(verbose_name='period number')
    startdate=models.DateField()
    enddate=models.DateField()
    num_days=models.IntegerField(default=30,verbose_name="Number of Days")
    p_flag=models.BooleanField(default=True)
    objects = models.Manager()

    class Meta:
        verbose_name_plural='periods'
    def __str__ (self):
        return self.period_name

class employee(models.Model):
    emp_name=models.CharField(max_length=200,verbose_name='employee name')
    staff_id_num=models.CharField(max_length=20,unique=True,verbose_name='UNRAID No.')
    emp_station=models.ForeignKey(station,on_delete=models.CASCADE)
    emp_position=models.ForeignKey(position,on_delete=models.CASCADE)
    emp_scale=models.ForeignKey(salaryscale,on_delete=models.CASCADE)
    date_left_org=models.DateField(null=True)
    objects = models.Manager()
    class Meta:
        verbose_name_plural='employees'
    def __str__ (self):
        return self.emp_name

class requistiondetailtype(models.Model):
    ## e.g request for NOA,SDA,Advance,expense claim
    detail_name=models.CharField(max_length=100)
    objects = models.Manager()
    class Meta:
        verbose_name_plural='requistiondetailtypes'
    def __str__ (self):
        return self.detail_name
class requistion(models.Model):
    made_by=models.ForeignKey(employee,on_delete=models.CASCADE)
    date_made=models.DateTimeField(auto_now_add=True)
    purpose=models.TextField(verbose_name='Purpose')
    objects = models.Manager()
    class Meta:
        verbose_name_plural='requistion'
    def __str__ (self):
        return self.purpose
class requistiondetail(models.Model):
    requistionid=models.ForeignKey(requistion,on_delete=models.CASCADE)
    emp_name=models.ForeignKey(employee,on_delete=models.CASCADE)
    detail_type=models.ForeignKey(requistiondetailtype,on_delete=models.CASCADE)
    period_claimed=models.ForeignKey(period,on_delete=models.CASCADE)
    ndays=models.IntegerField(default=0,verbose_name="Number of days")
    startdate=models.DateField(null=True)
    enddate=models.DateField(null=True)
    rate=models.FloatField(default=0.0,verbose_name='Allowances Rate')
    amount=models.FloatField(default=0.0,verbose_name='Amount')
    objects = models.Manager()
    class Meta:
        verbose_name_plural='requistiondetails'

class requistion_total(models.Model) :
    id=models.IntegerField(db_column='id',primary_key=True)
    date_made=models.DateField(db_column='date_made')
    purpose=models.CharField(max_length=400,db_column='purpose')
    made_by=models.ForeignKey(employee,on_delete=models.DO_NOTHING)
    total=models.FloatField(db_column='Total')   
    objects = models.Manager()
    def __str__ (self):
        return self.purpose
    class Meta:
        verbose_name_plural='requistion_totals'
        managed=False
        db_table = 'requistions_total'