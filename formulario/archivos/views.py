from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
# from .forms import UploadFileForm
from django.views import View
from .models import Estudiante, Archivos
from .forms import EstudianteForm
from django.shortcuts import get_object_or_404

#Las vistas responden  a las solicitudes web y devuelven respuestas web.

#Crear estudiante
class CrearEstudianteView(View):
    def get(self, request):
        form = EstudianteForm()
        return render(request, "crear_estudiante.html", {"form": form, "accion": "crear"})

    def post(self, request):
        form = EstudianteForm(request.POST, request.FILES)
        archivos = request.FILES.getlist("archivos")
        if form.is_valid():
            estudiante = form.save()
            for archivo in archivos:
                Archivos.objects.create(estudiante=estudiante, archivo=archivo)
            return redirect("lista_estudiantes")
        return render(request, "crear_estudiante.html", {"form": form, "accion": "crear"})

#Editar estudiante
class EditarEstudianteView(View):
    def get(self, request, estudiante_id):
        estudiante = get_object_or_404(Estudiante, id=estudiante_id)
        form = EstudianteForm(instance=estudiante)
        archivos = Archivos.objects.filter(estudiante=estudiante)
        return render(request, "crear_estudiante.html", {"form": form, "accion": "editar", "estudiante": estudiante, "archivos": archivos})

    def post(self, request, estudiante_id):
        estudiante = get_object_or_404(Estudiante, id=estudiante_id)
        form = EstudianteForm(request.POST, request.FILES, instance=estudiante)
        archivos = request.FILES.getlist("archivos")
        if form.is_valid():
            estudiante = form.save()
            for archivo in archivos:
                Archivos.objects.create(estudiante=estudiante, archivo=archivo)
            return redirect("lista_estudiantes")
        archivos_existentes = Archivos.objects.filter(estudiante=estudiante)
        return render(request, "crear_estudiante.html", {"form": form, "accion": "editar", "estudiante": estudiante, "archivos": archivos_existentes})

# Eliminar estudiante
def eliminar_estudiante(request, estudiante_id):
    estudiante = get_object_or_404(Estudiante, id=estudiante_id)
    if request.method == "POST":
        estudiante.delete()
        return redirect("crear_estudiante")
    archivos = Archivos.objects.filter(estudiante=estudiante)
    return render(request, "confirmar_eliminar.html", {"estudiante": estudiante, "archivos": archivos})


# Vista para listar todos los estudiantes
def lista_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    for estudiante in estudiantes:
        estudiante.archivos = Archivos.objects.filter(estudiante=estudiante)
    return render(request, "lista_estudiantes.html", {"estudiantes": estudiantes})