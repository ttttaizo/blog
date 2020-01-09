from django.db import models

# Create your models here.
class BlogModel(models.Model):
    title = models.CharField(blank=False, null=False, max_length=150)
    content = models.TextField(blank=True)
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title