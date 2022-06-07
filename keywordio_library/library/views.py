from django.shortcuts import render,redirect
from library.forms import LibraryForm
from library.models import Library

# Create your views here.
def emp(request):                           #creating book
    if request.method == "POST":
        form = LibraryForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = LibraryForm()
    return render(request, 'index.html', {'form': form})


def show(request):                          #reading book
    librarys = Library.objects.all()
    return render(request, "show.html", {'librarys': librarys})

def books(request):
    librarys = Library.objects.all()
    return render(request, "books.html", {'librarys': librarys})

def edit(request, id):                      #updating book
    library = Library.objects.get(id=id)
    return render(request, 'edit.html', {'library': library})
def about(request):
    librarys = Library.objects.all()
    return render(request, "home1.html", {'librarys': librarys})

def update(request, id):                    #updating book
    library = Library.objects.get(id=id)
    form = LibraryForm(request.POST, instance=library)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'library': library})

def destroy(request, id):                   #deleting book
    library = Library.objects.get(id=id)
    library.delete()
    return redirect("/show")