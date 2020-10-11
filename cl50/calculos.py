import subprocess, json


class Calculos:
    def cl50(cls, c, i, m):
        try:
            script = 'Rscript -e "source(\'teste.R\'); tsk(c'+c+','+i+',c'+m+');"'
            r = subprocess.check_output(script, shell=True)
            a = r.decode("utf-8")
            b = a.split(sep="#", maxsplit=5)
            result = {"code" : 1, "result" : { "cl50" : round(float(b[0]),2), "nem" : round(float(b[1]),2), "min" : round(float(b[2]),2), "max" : round(float(b[3]),2)}}
        except:
            result = {"code" : 0, "result" : { "msg" : "Ocorreu um erro no calculo!! Verifique os valores e tente novamente"}}

        return result


