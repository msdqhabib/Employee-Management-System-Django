from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_form, name='employee_form'), #GET,POST for insert creation
    path('<int:id>/', views.employee_form, name='employee_update'), #GET,POST for update 
    path('list/', views.employee_list, name='employee_list'), #GET to retrieve 
    path('delete/<int:id>/', views.employee_delete, name='employee_delete'), #Delete  
]