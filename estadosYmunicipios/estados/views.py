from django.http import JsonResponse
from django.shortcuts import render
from .models import Estado, Municipio

# Create your views here.
def index(request):
    estados = Estado.objects.all()
    return render(request, 'inicio.html', {'estados': estados})

def cargar_municipios(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        estado_id = request.GET.get('estado_id')
        municipios = list(Municipio.objects.filter(estado_id=estado_id).
                            values('id', 'nombre', 'habitantes'))
        return JsonResponse({'municipios': municipios})
    return JsonResponse({'error': 'Petición inválida'}, status=400)