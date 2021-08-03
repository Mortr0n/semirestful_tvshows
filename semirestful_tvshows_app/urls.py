from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('shows', views.shows),
    path('shows/new', views.new),
    path('shows/create', views.create),
    path('shows/<int:showID>', views.selected_show),
    
]
