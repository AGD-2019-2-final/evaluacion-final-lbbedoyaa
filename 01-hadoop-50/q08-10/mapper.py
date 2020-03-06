import sys
#
#  >>> Escriba el codigo del mapper a partir de este punto <<<
#

if __name__ == "__main__":

       for line in sys.stdin:
         c1,c2,c3 = line.split("   ")
         c3=c3.strip() ##Me quita los caracteres adiconales
                   
         sys.stdout.write("{},{}\n".format(c1,c3))