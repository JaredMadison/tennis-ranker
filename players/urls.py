from django.urls import path
from . import views

urlpatterns = [
    path("", views.player_index, name="player_index"),
    #path("<int:pk>/", views.project_detail, name="project_detail"),
]