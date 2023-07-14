from django.shortcuts import render
from .forms import ContactForm
from .models import Project, Education, Skill, WorkExperience, Testimonial


def home(request):
    return render(request, 'portfolio_app/home.html')


def about_me(request):
    message = "Write a brief introduction about yourself here."

    context = {
        'message': message,
    }

    return render(request, 'portfolio_app/about_me.html', context)


def projects(request):
    projects = Project.objects.all()

    context = {
        'projects': projects,
    }

    # Render the template with projects if available, or show "No projects available" message
    if projects.exists():
        return render(request, 'portfolio_app/projects.html', context)
    else:
        message = "No projects available"
        context['message'] = message
        return render(request, 'portfolio_app/projects.html', context)


def education(request):
    education = Education.objects.all()

    context = {
        'education': education,
    }

    return render(request, 'portfolio_app/education.html', context)


def skills(request):
    skills = Skill.objects.all()

    context = {
        'skills': skills,
    }

    return render(request, 'portfolio_app/skills.html', context)


def work_experience(request):
    work_experience = WorkExperience.objects.all()

    context = {
        'work_experience': work_experience,
    }

    return render(request, 'portfolio_app/work_experience.html', context)


def testimonials(request):
    testimonials = Testimonial.objects.all()

    context = {
        'testimonials': testimonials,
    }

    return render(request, 'portfolio_app/testimonials.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'portfolio_app/contact_success.html')
    else:
        form = ContactForm()

    return render(request, 'portfolio_app/contact.html', {'form': form})