from django.shortcuts import render
from .models import Logger

def log_list(request):
    logs = Logger.objects.all()
    return render(request, 'Logger/log_list.html',{'logs':logs})



