from django.contrib.auth import authenticate
from .models import Atleta


def add_variable_to_context(request):
    try:
        atleta = Atleta.objects.get(usuario=request.user)
    except:
        atleta = None

    return {'user': request.user, 'atleta': atleta}