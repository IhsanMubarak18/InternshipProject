from django.urls import path
from .import views

urlpatterns = [
    path('',views.background_view),
    path('studentRegister/',views.studentRegister_view,name='studentReg'),
    path('companyRegister/',views.companyRegister_view,name='companyReg'),
]
