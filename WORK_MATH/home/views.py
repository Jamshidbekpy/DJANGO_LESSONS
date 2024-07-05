from django.shortcuts import render
from home.models import Image_work, Form, Projects, Admin
from home.forms import UserForm
from django.shortcuts import get_object_or_404

def index(request):
    image_work = Image_work.objects.all()
    form_users = Form.objects.all()
    projects = Projects.objects.all()
    projects_count = projects.count()
    form_users_count = form_users.count()
    
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            context = {
                'image_work': image_work.order_by('-created_at')[:4],
                'user': user,
                'form_users_count': form_users_count,
                'projects_count': projects_count,
                'form': UserForm()  # Yangi bo'sh forma yuborish
            }
            return render(request, 'index.html', context)
    else:
        form = UserForm()

    context = {
        'image_work': image_work.order_by('-created_at')[:4],
        'form_users_count': form_users_count,
        'projects_count': projects_count,
        'form': form
    }
    return render(request, 'index.html', context)

def about(request, slug):
    image_work = Image_work.objects.all()
    photo = get_object_or_404(Image_work, slug=slug)
    context = {
        'image_work': image_work.order_by('-created_at')[:4],
        'photo': photo,
    }
    return render(request, 'index.html', context)

def learn_more(request, slug):
    admin = Admin.objects.all()
    name = get_object_or_404(Admin, slug=slug)
    context = {
        'admin': admin.order_by('-created_at')[:1],
        'name': name,
    }
    return render(request, 'index.html', context)



