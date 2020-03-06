-- Pregunta
-- ===========================================================================
-- 
-- Para el archivo `data.tsv` compute la cantidad de registros por letra de la 
-- columna 2 y clave de al columna 3; esto es, por ejemplo, la cantidad de 
-- registros en tienen la letra `b` en la columna 2 y la clave `jjj` en la 
-- columna 3 es:
-- 
--   ((b,jjj), 216)
-- 
-- Escriba el resultado a la carpeta `output` del directorio actual.
-- 
fs -rm -f -r output;
--
-- >>> Escriba su respuesta a partir de este punto <<<
--


u = LOAD 'data.tsv' USING PigStorage ('\t')
    AS (c1:CHARARRAY, 
       c2:BAG{t:TUPLE(p:CHARARRAY)}, 
       c3:MAP[]);
       
y= foreach u generate flatten(c2), flatten(c3);
y= group y by ($0, $1);

y= foreach y generate $0, COUNT(y);


STORE y INTO 'output' USING PigStorage ('\t');
fs -get output/ .