import subprocess, json


class Calculos:
    def cl50(cls, comando):
        # r = subprocess.check_output('Rscript -e "source(\'teste.R\'); tsk( c(0.52,0.91,1.60,2.81,4.92), 3, c(0,0,2,3,3));"' , shell=True)
        script = 'r/bin/rscript -e "source(\'teste.R\'); tsk('+comando+');"'
        r = subprocess.check_output(script, shell=True)
        a = r.decode("utf-8")
        b = a.split(sep="#", maxsplit=5)
        return b


