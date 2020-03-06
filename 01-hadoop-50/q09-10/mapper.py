import sys
#
#  >>> Escriba el codigo del mapper a partir de este punto <<<
#
if __name__ == "__main__":

      for line in sys.stdin:
        key, fecha, val= line.split("   ")
        val=val.strip()
        if len(val)!=3:
          for i in range(0,3-len(val)):
            val="0"+val

        sys.stdout.write("{}\t{}\t{}\n".format(val, key, fecha))