from django.contrib import admin
from backend.models import Number
from backend.models import Pokemon

# Register your models here.

class NumberAdmin(admin.ModelAdmin):
    list_display = ('number', 'letter')  # Campos que quieres mostrar en la lista
    search_fields = ('number', 'letter')  # Campos por los cuales quieres permitir la búsqueda

class PokemonAdmin(admin.ModelAdmin):
    list_display = ('name', 'pokedex_number', 'primary_type')  # Campos que quieres mostrar en la lista
    search_fields = ('name', 'pokedex_number')  # Campos por los cuales quieres permitir la búsqueda

admin.site.register(Number, NumberAdmin)
admin.site.register(Pokemon, PokemonAdmin)
