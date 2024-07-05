from django.db import models

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
    def created_at_format(self):
        return self.created_at.strftime('%Y-%m-%d %H:%M:%S')
    def updated_at_format(self):
        return self.updated_at.strftime('%Y-%m-%d %H:%M:%S')
    format_created_at = property(created_at_format)
    format_updated_at = property(updated_at_format)