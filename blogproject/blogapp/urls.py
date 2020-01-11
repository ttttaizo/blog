from django.urls import path, include
from .views import index, BlogDetail, BlogCreate

urlpatterns = [
    path('', index, name='index'),
    path('detail/<int:pk>', BlogDetail.as_view(), name='detail'),
    path('create/', BlogCreate.as_view(), name='create')
]