import sys
#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
if __name__ == '__main__':

    curkey = None
    counter=0

    ##
    ## cada linea de texto recibida es una
    ## entrada clave \tabulador valor
    ##
    for line in sys.stdin:

        key, val = line.split("\t")
        val = int(val)

        if key == curkey:
            ##
            ## No se ha cambiado de clave. Aca se
            ## acumulan los valores para la misma clave.
            ##
            sys.stdout.write(",{}".format(val))
        else:
            ##
            ## Se cambio de clave. Se reinicia el
            ## acumulador.
            ##
            sys.stdout.write("\n {}\t{}".format(key, val))
            curkey=key
            if curkey is None:
                ##
                ## una vez se han reducido todos los elementos
                ## con la misma clave se imprime el resultado en
                ## el flujo de salida
                ##
                curkey = key
