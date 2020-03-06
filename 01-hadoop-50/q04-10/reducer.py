import sys
#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#

if __name__ == '__main__':


    ##
    ## cada linea de texto recibida es una
    ## entrada clave \tabulador valor
    ##
    for line in sys.stdin:
      
      fecha, letra, val = line.split(",")
      val=val.strip()
      sys.stdout.write("{},{},{}\n".format(letra, fecha, val))