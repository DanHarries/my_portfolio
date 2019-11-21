from django.db import models

# Create your models here.
class JobDetail(models.Model):
    date_from_to = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    job_title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    date_published = models.DateTimeField('date published')
    
class JobDescription(models.Model):
    job_details = models.ForeignKey(JobDetail, on_delete=models.CASCADE)
    description = models.CharField(max_length=250)