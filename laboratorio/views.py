from pprint import pprint

from django.contrib import messages
from django.shortcuts import render, redirect

from .models import Personal, Equipo, Prestamo


# Create your views here.
def index(request):
    if request.method == 'GET':
        # si la petición es GET, obtenemos todos los equipos y los pasamos a la plantilla
        equipos = Equipo.objects.all().order_by('-id')
        return render(request, 'index.html', {'equipos': equipos})
    else:
        try:
            # si la petición es POST, obtenemos el nombre y la descripción del equipo
            nombre = request.POST.get('nombre')
            descripcion = request.POST.get('descripcion')
            # creamos un objeto Equipo con los datos obtenidos y lo guardamos en la base de datos
            equipo = Equipo(nombre=nombre, descripcion=descripcion)
            equipo.save()
            # mostramos un mensaje de éxito
            messages.success(request, 'Equipo creado con éxito')
            # redirigimos al usuario de vuelta a la página principal
            return redirect('index')
        except ValueError:
            # si ocurre un error al crear el equipo, mostramos un mensaje de error y volvemos a la página principal
            messages.error(request, 'Error al crear el equipo')
            return render(request, 'index.html')


def delete(request, equipo_id):
    # obtenemos el equipo correspondiente al id proporcionado
    equipo = Equipo.objects.get(id=equipo_id)
    # obtenemos el nombre del equipo para usarlo en el mensaje de éxito
    nombre = Equipo.objects.get(id=equipo_id).nombre
    # eliminamos el equipo de la base de datos
    equipo.delete()
    # mostramos un mensaje de éxito
    messages.success(request, 'Equipo ' + str(nombre) + ' eliminado con éxito')
    # redirigimos al usuario de vuelta a la página principal
    return redirect('index')
