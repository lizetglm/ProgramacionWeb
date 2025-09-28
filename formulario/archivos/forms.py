from django import forms


#permite subir multiples archivos
# class MultipleFileInput(forms.ClearableFileInput):
#     allow_multiple_selected = True

# class ArchivosForm(forms.Form):
#     nombre = forms.CharField(label="Nombre", max_length=100)
#     carrera = forms.CharField(label="Carrera", max_length=100)
#     semestre = forms.IntegerField(label="Semestre")
#     archivo = forms.FileField(label="Archivo")