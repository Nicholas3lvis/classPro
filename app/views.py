from django.shortcuts import render,redirect
from .models import Blog
from .models import Employ
from .forms import BlogForm 
from .forms import EmployForm
# Create your views here.

def home(request):
    return render (request,'app/index.html')

def about(request):
    posts = Blog.objects.all() 
    return render (request,'app/about.html',{'posts': posts})

def blog(request):
    posts = Blog.objects.all() 
    return render (request, 'app/blog.html',{'posts': posts})

def services(request):
    return render (request, 'app/services.html')

def portfolio(request):
    posts = Employ.objects.all()
    return render (request, 'app/portfolio.html',{'posts': posts})

def review(request):
    return render(request,'app/review.html')

def form(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog')
    else:
        form = BlogForm()
    
    return render(request, 'app/form.html', {'form': form})

def worker(request):
    if request.method == 'POST':
        form = EmployForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('portfolio')
    else:
        form = EmployForm()
    
    return render(request, 'app/worker.html', {'form': form})
