-- 
-- Pregunta
-- ===========================================================================
-- 
-- Para el archivo `data.tsv` compute la cantidad de registros por letra. 
-- Escriba el resultado a la carpeta `output` del directorio actual.
--

--fs -put data.tsv;

fs -rm -f -r output;
--
-- >>> Escriba su respuesta a partir de este punto <<<
--


u = LOAD 'data.tsv' USING PigStorage ('\t')
    AS (letra:CHARARRAY, 
       fecha:CHARARRAY, 
       valor:INT);
      
y= GROUP u BY letra;


z= FOREACH y GENERATE $0, COUNT($1);

--DUMP z;

-- fs -rmdir output
--fs -mkdir output

STORE z INTO 'output';
fs -get output/ .



