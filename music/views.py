# Views are simple functions that return HTML
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .models import Album
from .forms import UserForm

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


class UserFormView(View):
    form_class = UserForm  # Points to class UserForm in forms.py
    template_name = 'music/registration_form.html'

    def get(self, request):  # Displays blank form
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):  # Processes form data
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            # Cleaned, normalized data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # returns User objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('music:index')

        # If login fails, send to blank form
        return render(request, self.template_name, {'form': form})
