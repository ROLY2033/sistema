from django.http import HttpResponse
import datetime


def saludo(request): #primera vista
	return HttpResponse("El commit mas reciente")

def data(request):
	return HttpResponse("data form using")

def dameHora(request):
	fecha_actual = datetime.datetime.now()

	documento = """ 
	<html>
		<body>
			<h1>fecha y hora</h1>%s
		</body>
	</html>
	"""%fecha_actual

	return HttpResponse(documento)
