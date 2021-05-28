from django.shortcuts import redirect, render
from . import models
from django.contrib import messages

def root(request):

    return redirect('/shows')

def shows(request):

    context = {
        "shows" : models.getshows()
    }

    return render(request, "table.html", context)
     
def new(request):


    return render(request, "add.html")

def create(request):
    title = request.POST['title']
    network = request.POST['network']
    release_date = request.POST['release_date']
    description = request.POST['description']

    errors = models.Show.objects.basic_validator(title,network, release_date, description)

    if len(errors) > 0:
        
        for key, value in errors.items():
            messages.error(request, value)
       
        return redirect('/shows/new')

    else:

        models.create( title,network,release_date, description )

        id = models.Show.objects.last().id



    return redirect('/shows/' + str(id))

def showid(request, id):

    context = {
        "shows":models.Show.objects.get(id = int(id))
    }

    return render(request, 'show.html', context)

def edit(request, id):

    context  = {
        'show' : models.Show.objects.get(id = id)
    }

    return render(request, "edit.html", context)

def update(request, id):
    x =models.Show.objects.get(id = int(id))

    title = request.POST['title']
    network = request.POST['network']
    release_date = request.POST['release_date']
    description = request.POST['description']


    errors = models.Show.objects.basic_validator(title,network, release_date, description)

    if len(errors) > 0:
        
        for key, value in errors.items():
            messages.error(request, value)

        
       
        return redirect('/shows/' + str(id) +'/edit')

    else:

    
       


        x.title = request.POST['title']
        x.network = request.POST['network']
        # date=x.release_date
        # new_date=date.strftime("%Y-%m-%d %H:%M %p")
        x.release_date = request.POST['release_date']
        x.description = request.POST['description']
        x.save()

       
        

        id = x.id
    return redirect('/shows/' + str(id))

def destroy(request, id):

    x = models.Show.objects.get(id = id)
    x.delete()
  




    return redirect('/shows')