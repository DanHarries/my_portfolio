from django.db import models

# Create your models here.
class JobDetail(models.Model):
    date_from_to = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    job_title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    date_published = models.DateTimeField('date published')
    
    def __str__(self):
        return self.company_name
    
class JobDescription(models.Model):
    job_details = models.ForeignKey(JobDetail, on_delete=models.CASCADE, related_name='jobdetails')
    description = models.CharField(max_length=250)
    
    def __str__(self):
       return self.description