from django.contrib import admin

# Register your models here.
from home.models import News,NewsCategory


class NewsAdmin(admin.ModelAdmin):
    filter_horizontal = ('category',)
admin.site.register(News,NewsAdmin)
admin.site.register(NewsCategory)
