from django.db import models
from config.models import BaseModel

# Create your models here.
class Image_work(BaseModel):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    slug = models.SlugField(max_length=255, null=True, blank=True, unique=True)
    class Meta:
        verbose_name = "Image_work"
        verbose_name_plural = "Image_works"   
    def __str__(self):
        return self.name
class Form(BaseModel):                       #Our clients
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    
    class Meta:
        verbose_name = "Form"
        verbose_name_plural = "Forms"
    def __str__(self):
        return f"{self.name} - {self.email}"
    

class Projects(BaseModel):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
    def __str__(self):
        return self.name
class Admin(BaseModel):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    body = models.TextField()
    slug = models.SlugField(max_length=255, null=True, blank=True, unique=True)
    class Meta:
        verbose_name = "Admin"
        verbose_name_plural = "Admins"
    def __str__(self):
        return self.name

