from django.shortcuts import render, HttpResponse, redirect
from .models import Shows

def index(request):
    
    
    return render(request, 'index.html')

def shows(request):
    context = {
        'all_shows' : Shows.objects.all(),
    }
    return render(request, 'all_shows.html', context)

def new(request):
    
    return render(request, 'new_show.html')

def create(request):
    new_show = Shows.objects.create(
        title = request.POST['title_input'],
        network = request.POST['network_input'],
        release_date = request.POST['release_date_input'],
    )
    return redirect(f'/shows/{new_show.id}')

def selected_show(request, showID):
    selected_show = Shows.objects.get(id=showID)
    
    context = {
        'id' : selected_show.id,
        'title' : selected_show.title,
        'network' : selected_show.network,
        'release' : selected_show.release_date,
        
    }
    return render(request, 'selected_show.html', context)
