from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Project, Education, Skill, WorkExperience, Certification, Testimonial, ContactMessage


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'custom_field')


admin.site.register(Project)
admin.site.register(Education)
admin.site.register(Skill)
admin.site.register(WorkExperience)
admin.site.register(Certification)
admin.site.register(Testimonial)
admin.site.register(ContactMessage)