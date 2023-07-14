from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects', default='default_image.jpg')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title


class Education(models.Model):
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    honors = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.degree


class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    proficiency_level = models.IntegerField()

    def __str__(self):
        return self.name


class WorkExperience(models.Model):
    job_title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    responsibilities = models.TextField()
    achievements = models.TextField(blank=True)

    def __str__(self):
        return self.job_title


class Certification(models.Model):
    name = models.CharField(max_length=200)
    issuing_organization = models.CharField(max_length=200)
    completion_date = models.DateField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    name = models.CharField(max_length=200)
    affiliation = models.CharField(max_length=200)
    testimonial = models.TextField()
    photo = models.ImageField(upload_to='testimonials', blank=True)

    def __str__(self):
        return self.name


class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject