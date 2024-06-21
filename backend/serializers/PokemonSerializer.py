from rest_framework import serializers
from backend.models import Pokemon

class PokemonSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=20)
    pokedex_number = serializers.IntegerField(required=False)
    primary_type = serializers.CharField(max_length=100, required=False)
    secondary_type = serializers.CharField(max_length=100, required=False)

    class Meta:
        model = Pokemon
        fields = ['name', 'pokedex_number', 'primary_type', 'secondary_type']
