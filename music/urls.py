from django.urls import path
from . import views


app_name = 'music'

urlpatterns = [  # Looks for functions in views
    # /music/
    path('', views.IndexView.as_view(), name='index'),  # Using a class, but as_view() treats it as a function

    # /music/pk/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),

    # /music/album/add/
    path('album/add/', views.AlbumCreate.as_view(), name='album-add'),

    # /music/album/pk/
    path('album/<int:pk>/', views.AlbumUpdate.as_view(), name='album-update'),

    # /music/album/pk/delete/
    path('album/<int:pk>/delete/', views.AlbumDelete.as_view(), name='album-delete'),

]
