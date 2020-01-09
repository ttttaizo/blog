from django.urls import path, include
from .views import index, BlogDetail

urlpatterns = [
    path('', index, name='index'),
    path('detail/<int:pk>', BlogDetail.as_view(), name='detail'),
]