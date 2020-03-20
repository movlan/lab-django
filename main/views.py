from django.shortcuts import redirect, render
from django.http import request
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Dog, Toy
from .forms import FeedingForm


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
    toys_dog_doesnt_have = Toy.objects.exclude(id__in = dog.toys.all().values_list('id'))
    feeding_form = FeedingForm()
    return render( request, 'dog.html', {'dog': dog, 'feeding_form': feeding_form, 'toys': toys_dog_doesnt_have })

def add_feeding(request, dog_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.dog_id = dog_id
    new_feeding.save()
  return redirect('detail', dog_id=dog_id)

def toy_assoc(request, dog_id, toy_id):
    Dog.objects.get(id=dog_id).toys.add(toy_id)
    return redirect('detail', dog_id=dog_id)