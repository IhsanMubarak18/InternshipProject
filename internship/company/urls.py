from django.urls import path
from .import views

urlpatterns = [
    path('',views.companyRegister_view,name='companyReg')
    
]
