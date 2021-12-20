from django.http import HttpResponse

def saludo(request): #primera vista
	return HttpResponse("Hola alumnos")

def data(request):
	return HttpResponse("data form using")