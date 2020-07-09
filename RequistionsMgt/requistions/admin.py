from django.contrib import admin

# Register your models here.
from  .models import station,directorate,position,salaryscale,requesttype,ratetype,allowancerate,period,employee,requistiondetailtype,requistion,requistiondetail
class detailinline(admin.TabularInline):
    model=requistiondetail
@admin.register(requistion)
class requistionadmin(admin.ModelAdmin):
    inlines=[detailinline,]

admin.site.register(station)
admin.site.register(directorate)
admin.site.register(position)
admin.site.register(salaryscale)
admin.site.register(requesttype)
admin.site.register(ratetype)
admin.site.register(allowancerate)
admin.site.register(period)
admin.site.register(employee)
admin.site.register(requistiondetailtype)
#admin.site.register(requistion)
admin.site.register(requistiondetail)