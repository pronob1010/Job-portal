from django.contrib import admin
from.models import ContactUs,Website_Details,Job_categories,jobpost,freelancer_job,user_status,professional_profile,UserProfile,testimonials
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(ContactUs)
admin.site.register(Website_Details)
admin.site.register(Job_categories)
admin.site.register(jobpost)
admin.site.register(freelancer_job)
admin.site.register(user_status)
admin.site.register(professional_profile)
admin.site.register(testimonials)
 
