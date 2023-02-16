#from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics,filters
from pokemons import serializers

from .models import Pokemon
from .serializers import PokemonSerializer
from django_filters.rest_framework import DjangoFilterBackend

class PokemonFilter(generics.ListAPIView):
        queryset = Pokemon.objects.all()
        serializer_class = PokemonSerializer
        filter_backends = DjangoFilterBackend
        search_fields = ['nombre','tipo','naturaleza']

@api_view(['GET','POST'])
def api_pokemon_view(request):
    if request.method == 'GET':
        pokemons = Pokemon.objects.all()
        serializer = PokemonSerializer(pokemons,many=True)
        return Response(serializer.data)
    else:
        serializer = PokemonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
@api_view(['GET','PUT','DELETE'])
def pokemon_detail_view(request,pk):
    pokemon = Pokemon.objects.filter(id=pk).first()
    if pokemon:
        if request.method == 'GET':
            serializer = PokemonSerializer(pokemon)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = PokemonSerializer(pokemon,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        elif request.method == 'DELETE':
            pokemon.delete()
            return Response({'message':'Pokemon borrado'})
    return Response({'message':'No se encontró el pokemon'})