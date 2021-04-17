from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from . models import *

urlpatterns = [
    path('', views.index, name="index"),
    
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.register, name="register"),
    path('freelancer/', views.freelancer, name="freelancer"),

    path('jobs/', views.jobs.as_view(), name="jobs"),
    path('my_jobs/', views.my_jobs.as_view(), name="my_jobs"),
    path('userProfile/', views.userProfile, name="userProfile"),
    path('createjob/', views.createjob, name="createjob"),
    path('createjobasfreelancher/', views.createjobasfreelancher, name="createjobasfreelancher"),    
    path('freelancher_detail/<str:id>/', views.freelancher_detail, name="freelancher_detail"),

    path('jobs/<str:id>/', views.jobdetail, name="jobdetail"),
    path('apply_done/', views.apply_done, name="apply_done"),
    
    path('blog/', views.blog_index, name="blog"),
    path('blog_details/', views.blog_details, name="blog_details"),
    path('portfolio_grid/', views.portfolio_grid, name="portfolio_grid"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('editProfile/', views.editProfile, name="editProfile"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)