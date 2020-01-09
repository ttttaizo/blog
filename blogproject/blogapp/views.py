from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from .models import BlogModel

# Create your views here.
def index(request):
    blogs = BlogModel.objects.order_by('-created_datetime')
    return render(request, 'index.html', {'blogs': blogs})
    

class BlogDetail(DetailView):
    template_name = 'detail.html'
    model = BlogModel
