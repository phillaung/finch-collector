from django.shortcuts import render

finches = [
  {'name': 'Coco', 'breed': 'yellowtail', 'description': 'furry little demon', 'age': 3},
  {'name': 'Sunny', 'breed': 'parrot', 'description': 'gentle and loving', 'age': 2},
]

# Create your views here.
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def finches_index(request):
  return render(request, 'finches/index.html', {
    'finches': finches
  })