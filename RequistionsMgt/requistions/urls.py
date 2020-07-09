from django.urls import path
from . import views
app_name='requistions'
urlpatterns=[

path('',views.index,name='index'),
path('requistions/',views.requistion_list,name='requistion_list'),
path('requistions/<int:pk>',views.requistion_get,name='requistion_get'),
path('add_requistion/',views.new_requistion,name='new_requistion'),
path('requistion_detail/<int:requistion_id>',views.add_details,name='add_details')

]