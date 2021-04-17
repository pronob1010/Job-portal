from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
# from django.contrib.auth.models import AbstractUser


from django.conf import settings
# Create your models here.


class UserProfile(models.Model):
    TYPE=(
        ('Male','Male'),
        ('Female','Female'),
        ('Transgender','Transgender')
        )
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    Organization = models.BooleanField(default=False, null=True, blank=True)
    Gender = models.CharField(max_length=100, choices=TYPE,default=None)
    phone = models.CharField(max_length=15)
    self_bio = models.TextField(max_length=150)

class ContactUs(models.Model):
    name =  models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(max_length=1000)

    def __str__(self):
        return self.name
    
class Website_Details(models.Model):
    site_Title = models.CharField(max_length=200)
    site_Logo = models.ImageField(upload_to='media/images')
    site_background = models.ImageField(upload_to='media/images', null=True)
    site_Description = models.TextField(max_length=500)
    address = models.CharField(max_length=100, null= True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.site_Title
class Job_categories(models.Model):
    tittle = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,default=tittle)

    def slug(self):
        return slugify(self.title)

    def __str__(self):
        return self.tittle
    
class jobpost(models.Model):
    TYPE=(
        ('Full Time','Full Time'),
        ('Part Time','Part Time'),
        )
    job_provider = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True,related_name='author')
    job_title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100,default=job_title)
    job_category = models.ManyToManyField(Job_categories)
    job_type = models.CharField(max_length=100, choices=TYPE)
    Job_introduction = models.CharField(max_length=500)
    Job_thumbnail = models.ImageField(upload_to ='media/images', null=True, blank=True)
    Job_description = models.TextField(max_length=3000)
    Job_requirement = models.TextField(max_length=3000)
    Job_salary_range = models.TextField(max_length=100)
    Job_Location = models.CharField(max_length=1000, null=True)
    Year_of_experience = models.IntegerField()
    job_created = models.DateTimeField(default=now)
    job_deadline = models.DateTimeField(default=None, null=True)
    Candidates = models.ManyToManyField(User, null=True,blank=True)
    how_to_apply =  models.TextField(max_length=100, null=True, blank=True)
    

    def slug(self):
        return slugify(self.job_title)


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
    freelancer_slug = models.SlugField(max_length=100,default=freelancer_title)
    freelancer_level = models.CharField(max_length=100, choices=TYPE)
    freelancer_thumbnail = models.ImageField(upload_to='media/images', null=True)
    freelancer_description = models.TextField(max_length=3000)
    freelancer_expected_salary = models.IntegerField()
    freelancer_skills = models.TextField(max_length=3000)
    Year_of_experience = models.IntegerField()
    freelancer_created = models.DateTimeField(default=now)
    freelancer_free_for_work = models.BooleanField(default=False)
    freelancer_promotion = models.BooleanField(default=False)

    def slug(self):
        return slugify(self.freelancer_title)

    def __str__(self):
        return self.freelancer_title
class user_status(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    user_status_text = models.TextField(max_length=2000, null = True)
    user_image = models.ImageField(upload_to='media/images', null=True) 
    slug = models.SlugField(max_length=100,default=id)

    def slug(self):
        return slugify(self.id)

    def __str__(self):
        return self.user

class professional_profile(models.Model):
    TYPE=(
        ('Male','Male'),
        ('Female','Female'),
        ('Transgender','Transgender')
        )
    TYPE2=(
        ('Beginner','Beginner'),
        ('Intermediate','Intermediate'),
        ('Expart','Expart'),
        )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    professional_title= models.CharField(max_length=150)
    professional_Description = models.TextField(max_length=550)
    professional_skills = models.TextField(max_length=550)
    professional_Experience_level = models.TextField(max_length=50,choices=TYPE2)
    professional_skills = models.TextField(max_length=550)
    Total_Project =models.IntegerField(default=0)
    Join_Date =  models.DateTimeField(default=now)
    slug = models.SlugField(max_length=100)

    def slug(self):
        return slugify(self.professional_title)

class testimonials(models.Model):
    text = models.TextField(max_length=200, null=True, blank=True)
