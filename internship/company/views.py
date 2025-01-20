from django.shortcuts import render
from .models import companyRegister_model

# Create your views here.

def companyRegister_view(request):
    if request.POST:
        company_name=request.POST.get('company_name')
        registration_number=request.POST.get('registration_number')
        email=request.POST.get('email')
        phone_number=request.POST.get('phone_number')
        address=request.POST.get('address')
        industry_type=request.POST.get('industry_type')
        register=companyRegister_model(company_name=company_name,registration_number=registration_number,email=email,phone_number=phone_number,address=address,industry_type=industry_type)
        register.save()
    return render(request,'company_register.html')
