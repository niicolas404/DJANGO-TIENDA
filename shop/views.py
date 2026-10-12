from django.shortcuts import render
from .models import producto


def inicio(request):
	productos = producto.objects.all().order_by('nombre')
	return render(request, 'inicio.html', {'productos': productos})
