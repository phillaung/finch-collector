from django.shortcuts import render, redirect
from .models import Finch, Toy
from .forms import FeedingForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def finches_index(request):
  finches = Finch.objects.all()
  return render(request, 'finches/index.html', {
    'finches': finches
  })

def finches_detail(request, finch_id):
  finch = Finch.objects.get(id=finch_id)
  id_list = finch.toys.all().values_list('id')
  toys_finch_doesnt_have = Toy.objects.exclude(id__in=id_list)
  feeding_form = FeedingForm()
  return render(request, 'finches/detail.html', {
    'finch': finch,
    'feeding_form': feeding_form,
    'toys': toys_finch_doesnt_have
  })

def add_feeding(request, finch_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.finch_id = finch_id
        new_feeding.save()
    return redirect('detail', finch_id=finch_id)

def assoc_toy(request, finch_id, toy_id):
  Finch.objects.get(id=finch_id).toys.add(toy_id)
  return redirect('detail', finch_id=finch_id)

class FinchCreate(CreateView):
  model = Finch
  fields = ['name', 'description', 'age']
  success_url = '/finches'

class FinchUpdate(UpdateView):
  model = Finch
  fields = ['description', 'age']

class FinchDelete(DeleteView):
  model = Finch
  success_url = '/finches'