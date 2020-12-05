from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import User


@csrf_exempt
def registration(request):
    if request.method == "POST":
        name = request.POST.get('name')
        real_name = request.POST.get('real_name')
        password = request.POST.get('password')
        email = request.POST.get('email')
        send_report = request.POST.get('send_report')
        decline_report = request.POST.get('decline_report')
        proccessing_report = request.POST.get('proccessing_report')

        User.objects.create(
            name=name, 
            real_name=real_name,
            password = password, 
            email = email,
            send_report = send_report,
            decline_report = decline_report,
            proccessing_report = proccessing_report
            )
        return HttpResponse("")
        
    return HttpResponse("")


@csrf_exempt
def login(request):
    if request.method == "POST":
        name = request.POST.get('name')
        pass_ = request.POST.get('password')
        user_data = User.objects.get(name=name, password=pass_)
        print(user_data.name)
        
        some_data_to_dump = {
            'name': user_data.name,
            "real_name": user_data.real_name,
            "password" : user_data.password,
            "email" : user_data.email,
            "send_report" : user_data.send_report,
            "decline_report" : user_data.decline_report,
            "proccessing_report" : user_data.proccessing_report
        }
        data = json.dumps(some_data_to_dump)

        return HttpResponse(data, content_type='application/json')
        
    return HttpResponse("")