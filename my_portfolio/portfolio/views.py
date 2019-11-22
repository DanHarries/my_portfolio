from django.shortcuts import render
from .models import JobDetail, JobDescription
from django.core.mail import send_mail

# Create your views here.
def index(request):
  
    job_list = JobDetail.objects.values('id', 'date_from_to', 'company_name', 'job_title','location', 'url')            
    job_desc = JobDescription.objects.values('job_details_id', 'description')

    context = {'job_list': job_list, 'job_desc': job_desc}
  
    return render(request, 'index.html', context)

def email(request):
    name = request.POST.get('name')
    email_address = request.POST.get('email')
    subject = request.POST.get('subject')
    message = request.POST.get('message')
        
    if not name or not email_address or not subject or not message:
        print('error')
        return render(request, 'index.html', {            
            'error_message': "Please fill in all the fields",
        })
    else:
        return HttpResponseRedirect(reverse('index.html'))
        
    
    return render(request, 'index.html')