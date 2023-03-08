from django.http import HttpResponse
from django.shortcuts import render, redirect
from movieapp.models import Movies
from .forms import MovieForm


# Create your views here.
def index(request):
    movies = Movies.objects.all()
    context = {
        'movies_list': movies
    }
    return render(request, "index.html", context)


def details(request, movies_id):
    movies = Movies.objects.get(id=movies_id)
    return render(request, "details.html", {'movies': movies})

def add(request):
    if request.method == "POST":
        name = request.POST.get('name', )
        desc = request.POST.get('desc', )
        number = request.POST.get('number', )
        img = request.FILES['img']
        movies = Movies(name=name, desc=desc, number=number, img=img)
        movies.save()
        return redirect('/')
    return render(request, 'add.html')


def update(request, id):
    movies = Movies.objects.get(id=id)
    form = MovieForm(request.POST or None,request.FILES,instance=movies)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movies':movies})

def delete(request,id):
    if request.method=='POST':
        movies=Movies.objects.get(id=id)
        movies.delete()
        return redirect('/')
    return render(request,'delete.html')