from django.contrib import admin

# Register your models here.
from  .models import (
    Station,
    Directorate,
    Position,
    SalaryScale,
    RequestType,
    RateType,
    AllowanceRate,
    Period,
    Employee,
    RequisitionDetailType,
    Requisition,
    RequisitionDetail
)
class DetailInline(admin.TabularInline):
    model=RequisitionDetail
@admin.register(Requisition)
class RequisitionAdmin(admin.ModelAdmin):
    inlines=[DetailInline,]

admin.site.register(Station)
admin.site.register(Directorate)
admin.site.register(Position)
admin.site.register(SalaryScale)
admin.site.register(RequestType)
admin.site.register(RateType)
admin.site.register(AllowanceRate)
admin.site.register(Period)
admin.site.register(Employee)
admin.site.register(RequisitionDetail)
admin.site.register(RequisitionDetailType)

