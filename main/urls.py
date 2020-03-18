from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('dog/<int:dog_id>', views.dog, name='detail'),
    path('dog/create', views.DogCreate.as_view(), name='dog_create'),
    path('dog/<int:pk>/update', views.DogUpdate.as_view(), name='dogs_update'),
    path('dog/<int:pk>/delete', views.DogDelete.as_view(), name='dogs_delete'),
]
