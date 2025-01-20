from django.shortcuts import render
from .models import studentRegister_model
# Create your views here.




def studentRegister_view(request):
    if request.POST:
        name=request.POST.get('name')
        register_no=request.POST.get('register_no')
        department=request.POST.get('department')
        register_obj=studentRegister_model(name=name,register_no=register_no,department=department)
        register_obj.save()
    return render(request,'student_register.html')

