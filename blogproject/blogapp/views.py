from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, CreateView
from .models import BlogModel
from django.urls import reverse, reverse_lazy

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
    #詳細画面に遷移させる
    def get_success_url(self):
        return reverse('detail', kwargs={'pk': self.object.pk})
    # success_url = reverse_lazy('index')