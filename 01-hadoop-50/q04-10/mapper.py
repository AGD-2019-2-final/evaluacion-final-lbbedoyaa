import sys
#
#  >>> Escriba el codigo del mapper a partir de este punto <<<
#


if __name__ == "__main__":
    ##
    ## itera sobre cada linea de codigo recibida
    ## a traves del flujo de entrada
    ##
    for line in sys.stdin:
      letra, fecha, val = line.split("   ")
      val=val.strip()
        ##
        ## genera las tuplas palabra \tabulador 1
        ## ya que es un conteo de palabras
      sys.stdout.write("{},{},{}\n".format(fecha, letra, val))
            