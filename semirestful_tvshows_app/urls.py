from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('shows', views.shows),
    path('shows/new', views.new),
    path('shows/create', views.create),
    path('shows/<int:showID>', views.selected_show),
    path('shows/<int:showID>/edit', views.edit_show),
    path('shows/<int:showID>/update', views.update_show),
    path('shows/<int:showID>/delete', views.delete_show)
    
]
