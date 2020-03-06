import sys
#
#  >>> Escriba el codigo del mapper a partir de este punto <<<
#
if __name__ == '__main__':
    counter=0
    for line in sys.stdin:
        
        if counter<6:
          val, key, fecha = line.split("\t")
          fecha=fecha.strip()
          val = int(val)
          sys.stdout.write("{}\t{}\t{}\n".format(key, fecha, val))
          counter=counter+1
        else:
          break