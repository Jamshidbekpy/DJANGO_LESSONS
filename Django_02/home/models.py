from django.db import models

# Create your models here.
class NewsCategory(models.Model):
    name = models.CharField(max_length=150)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    
class News(models.Model):
    category = models.ManyToManyField(NewsCategory)
    create_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    cart  = models.ImageField(default=None, upload_to='news/', height_field=None, width_field=None, max_length=None,null = True,blank = True)
    video = models.URLField(null = True,blank = True)
    desc = models.TextField()
    body = models.TextField()
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'new'
        verbose_name_plural = 'news'
    