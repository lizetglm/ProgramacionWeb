from django import forms
from .models import Estudiante

#permite subir multiples archivos
class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

#permite recibir multiples archivos
class MultipleFileField(forms.FileField):
    widget = MultipleFileInput(attrs={"multiple": True})

    #valida que los archivos sean pdf o imagenes
    def clean(self, data, initial=None):
        #data puede ser una lista o un solo archivo
        if not data:
            return []
        if not isinstance(data, (list, tuple)):
            data = [data]
        for file in data:
            if file.content_type not in ["application/pdf", "image/jpeg", "image/png"]:
                raise forms.ValidationError("Solo se permiten archivos PDF o imágenes (JPG, PNG, PNG).")
        return data

#formulario para el modelo Estudiante
class EstudianteForm(forms.ModelForm):
    archivos = MultipleFileField(required=False)

    class Meta:
        model = Estudiante
        fields = ["nombre", "carrera", "semestre"]