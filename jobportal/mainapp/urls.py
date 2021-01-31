from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name="index"),
    path('jobs/', views.jobs, name="jobs"),
    path('my_jobs/', views.jobs, name="my_jobs"),
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.register, name="register"),
    path('freelancer/', views.freelancer, name="freelancer"),

    path('jobdetail/', views.jobdetail, name="jobdetail"),
    path('apply_done/', views.apply_done, name="apply_done"),
    
    path('blog/', views.blog_index, name="blog"),
    path('blog_details/', views.blog_details, name="blog_details"),
    path('portfolio_grid/', views.portfolio_grid, name="portfolio_grid"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('userProfile/', views.userProfile, name="userProfile"),
    path('editProfile/', views.editProfile, name="editProfile"),
    path('createjob/', views.createjob, name="createjob"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)