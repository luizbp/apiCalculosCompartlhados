from cl50.calculos import Calculos

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser


@api_view(['POST'])
@parser_classes([JSONParser])
def calculo_cl50_json(request):
    if request.method == 'POST':
    
        try:
            concentracoes = request.data['c']
            individuos = request.data['i']
            mortalidades = request.data['m']
            c = Calculos()
            result = c.cl50(c=concentracoes, i=individuos, m=mortalidades)
            return Response({'response' : result})
        except:
            return Response({'response' : {"code" : 0, "result" : {"msg" : """
                Envie as informações no padrão abaixo:
                {
                    "c" : "( *concentrações separas por "," *)",
                    "i" : "*Quantidade de individuos por concentração ex:"5" *",
                    "m" : "(*mortalidade separadas por "," na ordem das concentrações *)"
                }
            """}}})

        # return Response({'CL50':round(float(result[0]),2), 'NEM':round(float(result[1]),2), 'min':round(float(result[2]),2), 'max':round(float(result[3]),2)})

