from django.shortcuts import render
from .models import Protfolio,Contact,MyArea,Setting
from django.http import JsonResponse

# Create your views here.
def home(request):
    if request.method == 'GET':
        protfolio = Protfolio.objects.all()
        total_development = Protfolio.objects.filter(project_type="development")
        total_design = Protfolio.objects.filter(project_type="design")
        total_mobile = Protfolio.objects.filter(project_type="mobile")
        my_area = MyArea.objects.all().order_by('id')
        settings = Setting.objects.all()
        context = {
            'data':protfolio,
            "total_development":total_development,
            "total_design":total_design,
            "total_mobile":total_mobile,
            "myArea":my_area,
            "settings":settings,
        }
        return render(request,'index.html', context=context)
    if request.method == 'POST':
        full_name = request.POST.get("fullName")
        email = request.POST.get("email")
        message = request.POST.get("message")
        data = Contact(full_name=full_name,email=email,message=message)
        data.save()
        return JsonResponse({
            "msg":"Success"  
        })

    return render(request,'index.html')