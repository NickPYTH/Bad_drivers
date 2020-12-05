from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import User


@csrf_exempt
def image_upload(request):
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

        some_data_to_dump = {
        'status': 'foo',
        }
        data = json.dumps(some_data_to_dump)

        #return HttpResponse(data, content_type='application/json')
        return HttpResponse("Hello World!")
        
    return HttpResponse("Hello World!")
