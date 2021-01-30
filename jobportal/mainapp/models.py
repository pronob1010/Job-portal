from django.db import models
 
# Create your models here.
class ContactUs(models.Model):
    name =  models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(max_length=1000)

    def __str__(self):
        return self.name
    
class Website_Details(models.Model):
    site_Title = models.CharField(max_length=200)
    site_Logo = models.ImageField(upload_to='MEDIA')
    site_background = models.ImageField(upload_to='MEDIA', null=True)
    physical_address = models.CharField(max_length=500, blank = True)
    site_Description = models.TextField(max_length=500)

    def __str__(self):
        return self.site_Title