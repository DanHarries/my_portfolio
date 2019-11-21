from django.contrib import admin
from .models import JobDetail, JobDescription
 
admin.site.site_header = "My Portfolio Admin" 
admin.site.site_title = "My Portfolio Admin Area" 
admin.site.index_title = "Welcome to My Portfolio Admin" 
 
class JobDescInline(admin.TabularInline):
    model = JobDescription
    extra = 1
    
class JobDetailAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['date_from_to', 'company_name', 'job_title', 'location', 'url' ]}), 
                 ('Date Information', {'fields': ['date_published'], 'classes':['collapse']}),]
    inlines = [JobDescInline]

admin.site.register(JobDetail, JobDetailAdmin)
