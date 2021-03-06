from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('dog/<int:dog_id>', views.dog, name='detail'),
    path('dog/create', views.DogCreate.as_view(), name='dog_create'),
    path('dog/<int:pk>/update', views.DogUpdate.as_view(), name='dogs_update'),
    path('dog/<int:pk>/delete', views.DogDelete.as_view(), name='dogs_delete'),
    path('dog/<int:dog_id>/add_feeding', views.add_feeding, name='add_feeding'),
    path('dog/<int:dog_id>/toy_assoc/<int:toy_id>', views.toy_assoc, name='toy_assoc'),
    path('dog/<int:dog_id>/add_photo', views.add_photo, name='add_photo'),
    path('dog/<int:dog_id>/unassoc_toy/<int:toy_id>/', views.unassoc_toy, name='unassoc_toy'),
    path('accounts/signup/', views.signup, name='signup'),
    path('toys/', views.ToyList.as_view(), name='toys_index'),
    path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
    path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
    path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
    path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),
]
