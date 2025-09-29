from django.urls import path

from .views import CrearEstudianteView, EditarEstudianteView, eliminar_estudiante, lista_estudiantes

urlpatterns = [
    path("", lista_estudiantes, name="lista_estudiantes"),
    path("estudiante/crear/", CrearEstudianteView.as_view(), name="crear_estudiante"),
    path("estudiante/editar/<int:estudiante_id>/", EditarEstudianteView.as_view(), name="editar_estudiante"),
    path("estudiante/eliminar/<int:estudiante_id>/", eliminar_estudiante, name="eliminar_estudiante"),
]