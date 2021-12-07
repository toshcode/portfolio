from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField
import re

Rating_range = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
]


# Create your models here.
class User(AbstractUser):
    pass

class Information(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=70, blank=True, null=True)
    bio = models.CharField(max_length=500, blank=True, null=True)
    about = models.TextField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=40, blank=True, null=True)
    email = models.EmailField(max_length=70, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    avatar = CloudinaryField('image', blank=True, null=True)
    resume = models.FileField(upload_to='resume', blank=True, null=True)

    #social networks
    github = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    other = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.full_name


class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    year = models.CharField(max_length=15, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    institution = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['-year']

    def __str__(self):
        return f"{self.user} => {self.title} from {self.institution}"


class Experience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    year = models.CharField(max_length=15, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['-year']

    def __str__(self):
        return f"{self.user} => {self.title} from {self.company}"


class Skillset(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True, null=True)
    imagelink = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    skill_rank = models.CharField(choices=Rating_range, default='2', max_length=15)

    class Meta:
        ordering = ['-skill_rank']

    def __str__(self):
        return f"{self.user} => {self.title}"

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True, null=True)
    slug =  models.SlugField(max_length=500, blank=True, null=True, unique=True)
    imagelink = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    project_rating = models.CharField(choices=Rating_range, default='2', max_length=15)
    demo = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)

    class Meta:
        ordering = ['-project_rating']

    def __str__(self):
        return f"{self.user} => {self.title}"

    def get_project_absolute_url(self):
        return "/projects/{}".format(self.slug)

    def save(self, *args, **kwargs):
        self.slug = self.slug_generate()
        super(Project, self).save(*args, **kwargs)

    def slug_generate(self):
        slug = self.title.strip()
        slug = re.sub("", "_", slug)
        return slug.lower()


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(max_length=100, blank=False, null=False)
    message = models.TextField(blank=True, null=True)
    subject = models.CharField(max_length=300, blank=False, null=False)
    send_time = models.DateField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-send_time']

    def __str__(self):
        return f"{self.user} => {self.subject}"