import sys
#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
if __name__ == "__main__":

      for line in sys.stdin:
        key, valores= line.split("\t")
        valores=valores.strip()
        for i in range(0,2-len(key)):
            key="0"+key
        for val in valores.split(","):
          
          sys.stdout.write("{}\t{}\n".format(val, key))        