from django.shortcuts import render
from .models import Job
from django.http import HttpResponse

def index(request):
    context={}
    jobs = Job.objects.all()
    context['jobs'] = jobs
    return render(request, 'jobs/index.html',context)
