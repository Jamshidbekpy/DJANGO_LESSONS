from django.contrib import admin
from home.models import Image_work, Form, Projects, Admin
# Register your models here.
@admin.register(Image_work)
class image_workAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Form)
class FormAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'email', )


@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'image')
    
@admin.register(Admin)
class AdminAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'email', 'title', 'body')
    prepopulated_fields = {'slug': ('name',)}

