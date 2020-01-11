from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, CreateView
from .models import BlogModel
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    blogs = BlogModel.objects.order_by('-created_datetime')
    return render(request, 'index.html', {'blogs': blogs})
    
class BlogDetail(DetailView):
    template_name = 'detail.html'
    model = BlogModel

class BlogCreate(CreateView):
    template_name = 'create.html'
    model = BlogModel
    fields = {'title', 'content'}
    success_url = reverse_lazy('index')