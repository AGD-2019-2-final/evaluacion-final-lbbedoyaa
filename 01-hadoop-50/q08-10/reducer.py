import sys
#
#  >>> Escriba el codigo del mapper a partir de este punto <<<
#
suma= 0
promedio=0
registros=0
curkey=None ##clave actual

for line in sys.stdin:

    key, val = line.split(",")
    val=float(val)

    if key == curkey:
        suma=suma+val
        registros=registros+1
        promedio= suma/registros
        
    else:
        
        if curkey is not None:
          sys.stdout.write("{}\t{}\t{}\t\n".format(curkey,suma,round(promedio, 3)))
            
        curkey=key
        suma=val
        promedio= val
        registros=1

sys.stdout.write("{}\t{}\t{}\t\n".format(curkey,suma,round(promedio, 3)))