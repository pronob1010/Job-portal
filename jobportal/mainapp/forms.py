from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import *

class RegistrationForm(UserCreationForm):
    extra_field = forms.BooleanField(label ='Organization', required=False)
    class Meta:
        model =User
        fields = ('first_name', 'last_name', 'username', 'email',)

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['extra_field']

class jobpostForm(forms.ModelForm):
    class Meta:
        model = jobpost
        exclude  = ('job_provider','Candidates','job_created')

class jobpostFormForFree(forms.ModelForm):
    class Meta:
        model = freelancer_job
        exclude  = ('freelancer_slug','freelancer_profile')
        

class my_profileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'