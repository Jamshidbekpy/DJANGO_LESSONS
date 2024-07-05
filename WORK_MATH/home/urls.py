from django.urls import path
from home.views import index, about, learn_more

app_name = 'home'

urlpatterns = [
    path('', index, name='index'),
    path('about/<slug:slug>/', about, name='about'),
    path('learnmore/<slug:slug>/', learn_more, name='learnmore'),
    # path('form/', form, name='form'),
]
