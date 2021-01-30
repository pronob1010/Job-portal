from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
# Create your models here.
class ContactUs(models.Model):
    name =  models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(max_length=1000)

    def __str__(self):
        return self.name
    
class Website_Details(models.Model):
    site_Title = models.CharField(max_length=200)
    site_Logo = models.ImageField(upload_to='media')
    site_background = models.ImageField(upload_to='media', null=True)
    physical_address = models.CharField(max_length=500, blank = True)
    site_Description = models.TextField(max_length=500)

    def __str__(self):
        return self.site_Title
class Job_categories(models.Model):
    tittle = models.CharField(max_length=100)

    def __str__(self):
        return self.tittle
    
class jobpost(models.Model):
    TYPE=(
        ('Full_time','Full_time'),
        ('Part_time','Part_time'),
        )
    Job_provider = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    job_title = models.CharField(max_length=200)
    job_category = models.ManyToManyField(Job_categories)
    job_type = models.CharField(max_length=100, choices=TYPE)
    Job_introduction = models.CharField(max_length=500)
    Job_thumbnail = models.ImageField(upload_to='media', null=True)
    Job_description = models.TextField(max_length=3000)
    Job_requirement = models.TextField(max_length=3000)
    Job_salary_range = models.TextField(max_length=100)
    Job_Location = models.CharField(max_length=1000, null=True)
    Year_of_experience = models.IntegerField()
    job_created = models.DateTimeField(default=now)

    def __str__(self):
        return self.job_title

class freelancer_job(models.Model):
    TYPE=(
        ('Beginner','Beginner'),
        ('Intermediate','Intermediate'),
        ('Expart','Expart'),
        )
    freelancer_profile = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    freelancer_title = models.CharField(max_length=200)
    freelancer_level = models.CharField(max_length=100, choices=TYPE)
    freelancer_thumbnail = models.ImageField(upload_to='media', null=True)
    freelancer_description = models.TextField(max_length=3000)
    freelancer_expected_salary = models.IntegerField()
    freelancer_skills = models.TextField(max_length=3000)
    Year_of_experience = models.IntegerField()
    freelancer_created = models.DateTimeField(default=now)
    freelancer_free_for_work = models.BooleanField(default=False)
    freelancer_promotion = models.BooleanField(default=False)

    def __str__(self):
        return self.job_title
class user_status(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    user_status_text = models.TextField(max_length=2000, null = True)
    user_image = models.ImageField(upload_to='media', null=True)  

class User(models.Model):
    TYPE=(
        ('Male','Male'),
        ('Female','Female'),
        ('Transgender','Transgender')
        )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Gender = models.CharField(max_length=100, choices=TYPE)
    phone = models.CharField(max_length=15)
    self_bio = models.TextField(max_length=150)
    
