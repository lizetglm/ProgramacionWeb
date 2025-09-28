from django import forms
from .models import Estudiante, Archivos


#permite subir multiples archivos
class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


#permite recibir multiples archivos
class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput(attrs={"multiple": True}))
        super().__init__(*args, **kwargs)

#validar los datos del formulario
    def clean(self, data, initial=None):
        files = super().clean(data, initial)
        if not isinstance(data, (list, tuple)):
            data = [data]
        for file in data:
            if not file.content_type in ["application/pdf", "image/jpeg", "image/png"]:
                raise forms.ValidationError("Solo se permiten archivos PDF o imágenes (JPG, PNG).")
        return data


#formulario para el modelo Estudiante
class EstudianteForm(forms.ModelForm):
    archivos = MultipleFileField(required=False)
    
    class Meta:
        model = Estudiante
        fields = ["nombre", "carrera", "semestre", "archivos"]