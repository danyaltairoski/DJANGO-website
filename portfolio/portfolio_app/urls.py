from django.urls import path
from . import views

app_name = 'portfolio_app'

urlpatterns = [
    path('about-me/', views.about_me, name='about-me'),
    path('projects/', views.projects, name='projects'),
    path('education/', views.education, name='education'),
    path('skills/', views.skills, name='skills'),
    path('work-experience/', views.work_experience, name='work-experience'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('contact/', views.contact, name='contact'),
]