from cl50.calculos import Calculos

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.http import JsonResponse


@api_view(['GET'])
def calculo_cl50(request, comando):
    if request.method == 'GET':
        c = Calculos()
        result = c.cl50(comando=comando)
        return JsonResponse({'CL50':round(float(result[0]),2), 'NEM':round(float(result[1]),2), 'min':round(float(result[2]),2), 'max':round(float(result[3]),2)})

@api_view(['GET','POST'])
def teste(request):
    if request.method == 'POST':
        return Response(request.data)