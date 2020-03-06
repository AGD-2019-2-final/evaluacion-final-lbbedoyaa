import sys
#
#  >>> Escriba el codigo del mapper a partir de este punto <<<
#
if __name__ == '__main__':


    ##
    ## cada linea de texto recibida es una
    ## entrada clave \tabulador valor
    ##
    for line in sys.stdin:
      
      letra, val, fecha = line.split(",")
      fecha=fecha.strip()
      sys.stdout.write("{},{},{}\t\n".format(letra, fecha, val))