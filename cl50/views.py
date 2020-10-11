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
            if(result['result']['code'] != 0): #Se o calculu não retornou nenhum erro
                return Response({'response' : result})
            else:
                return Response({'response' : result}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'response' : {"result" : {"msg" : """
                Envie as informações no padrão abaixo:
                {
                    "c" : "( *concentrações separas por "," *)",
                    "i" : "*Quantidade de individuos por concentração ex:"5" *",
                    "m" : "(*mortalidade separadas por "," na ordem das concentrações *)"
                }
            """}}}, status=status.HTTP_400_BAD_REQUEST)

