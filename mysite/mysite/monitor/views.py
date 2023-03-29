from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required


# Create your views here.
from django.http import HttpResponse

@login_required(login_url='common:login')
def index(request):
    rsyslogs = SystemEvents.objects.order_by('-id')[:10]
    context = {"rsyslogs":rsyslogs}
    return render(request, 'monitor/index.html',context)

@login_required(login_url='common:login')
def detail(request,data_id):
    rsyslogs = SystemEvents.objects.get(id=data_id)
    context = {"rsyslogs":rsyslogs}
    return render(request, 'monitor/detail.html',context)