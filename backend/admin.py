from django.contrib import admin
from backend.models import Number

# Register your models here.

class NumberAdmin(admin.ModelAdmin):
    list_display = ('number', 'letter')  # Campos que quieres mostrar en la lista
    search_fields = ('number', 'letter')  # Campos por los cuales quieres permitir la búsqueda

admin.site.register(Number, NumberAdmin)
