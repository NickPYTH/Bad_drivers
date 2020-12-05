from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import User, Report


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

@csrf_exempt
def push_report(request):
    if request.method == "POST":
        name = request.POST.get('name')
        desc = request.POST.get('description')
        car_number = request.POST.get('car_number')
        image1 = request.FILES["image1"]
        image2 = request.FILES["image2"]
        image3 = request.FILES["image3"]
        image1_link = request.POST.get('image1_link')
        image2_link = request.POST.get('image2_link')
        image3_link = request.POST.get('image3_link')
        Report.objects.create(
            user_name = name, 
            description = desc,
            image1 = image1,
            image2 = image2,
            image3 = image3,
            image1_link = image1_link,
            image2_link = image2_link,
            image3_link = image3_link,
            car_number = car_number,
            )
        return HttpResponse("")
        
    return HttpResponse("")

@csrf_exempt
def pull_report(request):
    if request.method == "POST":
        name = request.POST.get('name')
        user_data = Report.objects.filter(user_name=name)
        length, records = {}, {}
        tmp_lst = []
        tmp_dic = {}
        length['len'] = len(user_data)
        records['len'] = length['len']
        for i in range(len(user_data)):
            tmp_dic["user_name" ] = user_data[i].user_name
            tmp_dic["description"]= user_data[i].description
            tmp_dic["car_number" ]= user_data[i].car_number
            tmp_dic["image1_link"]= user_data[i].image1_link
            tmp_dic["image2_link"]= user_data[i].image2_link
            tmp_dic["image3_link"]= user_data[i].image3_link
            records[i] = tmp_dic

        print(records)
        data = json.dumps(records)

        return HttpResponse(data, content_type='application/json')
        
    return HttpResponse("")