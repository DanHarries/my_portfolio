from django.shortcuts import render
from .models import JobDetail, JobDescription

# Create your views here.
def index(request):
    
    job_list = JobDetail.objects.all()
    
    jobdesc = JobDescription.objects.select_related('job_details_id')
    print(jobdesc)
    context = {'job_list': job_list}
    
    return render(request, 'index.html', context)
