from django.urls import path
from .views import CrearEstudianteView, detalle_estudiante

urlpatterns = [
    path("estudiante/crear/", CrearEstudianteView.as_view(), name="crear_estudiante"),
    path("estudiante/<int:estudiante_id>/", detalle_estudiante, name="detalle_estudiante"),
]