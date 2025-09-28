from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
# from .forms import UploadFileForm
from django.views import View
from .models import Estudiante, Archivos
from .forms import EstudianteForm

#Las vistas responden  a las solicitudes web y devuelven respuestas web.
class CrearEstudianteView(View):
    def get(self, request):
        form = EstudianteForm()
        return render(request, "crear_estudiante.html", {"form": form})

    def post(self, request):
        form = EstudianteForm(request.POST, request.FILES)

        if form.is_valid():
            # Guardar estudiante
            estudiante = form.save(commit=False)
            estudiante.save()

            # Guardar archivos
            archivos = request.FILES.getlist("archivos")
            for archivo in archivos:
                Archivos.objects.create(estudiante=estudiante, archivo=archivo)

            return redirect("detalle_estudiante", estudiante_id=estudiante.id)

        return render(request, "crear_estudiante.html", {"form": form})
