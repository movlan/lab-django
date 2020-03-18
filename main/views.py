from django.shortcuts import render
from django.http import request
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Dog


class DogCreate(CreateView):
    model = Dog
    fields = '__all__'

class DogUpdate(UpdateView):
    model = Dog
    fields = ['breed', 'description', 'age']

class DogDelete(DeleteView):
    model = Dog
    success_url = '/'

def home(request):
    dogs = Dog.objects.all()
    return  render(request, 'home.html', { 'dogs': dogs})

def dog(request, dog_id):
    dog = Dog.objects.get(id=dog_id)
    return render(request, 'dog.html', {'dog': dog})

