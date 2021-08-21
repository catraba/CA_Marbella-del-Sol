from django.contrib import admin

from .models import Atleta, Marca

# Register your models here.

class AtletaAdmin(admin.ModelAdmin):
    readonly_fields = ('categoria', )

admin.site.register(Atleta, AtletaAdmin)
admin.site.register(Marca)