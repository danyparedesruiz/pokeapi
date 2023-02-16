from django.urls import path
from .views import api_pokemon_view,pokemon_detail_view
urlpatterns = [
    path('pokemon/',api_pokemon_view),
    path('pokemon/<int:pk>',pokemon_detail_view),
]
