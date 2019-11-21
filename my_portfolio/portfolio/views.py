from django.shortcuts import render
from .models import JobDetail, JobDescription
from django.db.models import Count

# Create your views here.
def index(request):
    result = dict()
    job_list = JobDetail.objects.values('id', 'date_from_to', 'company_name', 'job_title','location', 'url')            
    job_desc = JobDescription.objects.values('job_details_id', 'description')

 
    for job in job_list:        
        for item in job_desc:
            if(item['job_details_id'] == job['id']):
                print({**job, **item})
                    
                          
    print(result)           
   
          
    context = {'job_list': job_list, 'job_desc': job_desc}
  
    return render(request, 'index.html', context)

    