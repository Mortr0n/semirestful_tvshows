from django.shortcuts import render, HttpResponse, redirect
from .models import Shows

def index(request):
    
    
    return redirect('/shows')

def shows(request):
    context = {
        'all_shows' : Shows.objects.all(),
    }
    return render(request, 'all_shows.html', context)

def new(request):
    
    return render(request, 'new_show.html')

def create(request):
    if request.method == 'POST':
        new_show = Shows.objects.create(
            title = request.POST['title_input'],
            network = request.POST['network_input'],
            release_date = request.POST['release_date_input'],
            desc = request.POST['desc_input'],
    )
    return redirect(f'/shows/{new_show.id}')

# TODO: Get help with finding why description isn't working
def selected_show(request, showID):
    selected_show = Shows.objects.get(id=showID)
    context = {
        'id' : selected_show.id,
        'title' : selected_show.title,
        'network' : selected_show.network,
        'release' : selected_show.release_date,
        'description' : selected_show.desc,
    }
    return render(request, 'selected_show.html', context)

# TODO: possibly reduce the context to include variable as well
def edit_show(request, showID):
    if request.method == 'GET':
        current_show = Shows.objects.get(id=showID)
        context = {
            'current_show' : current_show,
        }
    return render(request, 'edit_show.html', context)
        

def update_show(request, showID):
    
    if request.method == 'POST': 
        current_show = Shows.objects.get(id=showID)       
        current_show.title = request.POST['title_input']
        current_show.network = request.POST['network_input']
        current_show.release_date = request.POST['release_date_input']
        current_show.desc = request.POST['desc_input']
        current_show.save()
    return redirect(f'/shows/{current_show.id}')
    


def delete_show(request, showID):
    if request.method == 'POST':
        current_show = Shows.objects.get(id=showID)
        current_show.delete()
    return redirect('/shows')
    
