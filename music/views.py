# Views are simple functions that return HTML
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Album

class IndexView(generic.ListView):
    # generic.ListView displays a list of objects
    template_name = 'music/index.html'  # Whenever you get a list of all the albums, they get put into this template.

    def get_queryset(self):
        # Return all the Albums
        # Default returns an object called object_list. (override by creating variable called context_object_list = 'xyz')
        return Album.objects.all()


class DetailView(generic.DetailView):
    # generic.DetailView displays a detail page of a particular object
    model = Album  # Looks in models.py at the Album model
    template_name = 'music/detail.html'  # Uses this template


class AlbumCreate(CreateView):  # A view that displays a form for creating an object
    # Refers to album_form.html
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']  # Fields required


class AlbumUpdate(UpdateView):  # A view that displays a form for editing an object
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']


class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')  # After successfully deleting an object, redirects to home page
