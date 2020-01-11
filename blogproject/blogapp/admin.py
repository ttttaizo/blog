from django.contrib import admin
from .models import BlogModel
from django.contrib.admin.options import (
    HORIZONTAL, VERTICAL, ModelAdmin, StackedInline, TabularInline,
)

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'created_datetime', 'updated_datetime')
    list_display_links = ('id', 'title')

admin.site.register(BlogModel, BlogAdmin)
    