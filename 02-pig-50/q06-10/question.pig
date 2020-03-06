-- 
-- Pregunta
-- ===========================================================================
-- 
-- Para el archivo `data.tsv` Calcule la cantidad de registros por clave de la 
-- columna 3. En otras palabras, cuántos registros hay que tengan la clave 
-- `aaa`?
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
       
y= foreach u generate flatten(c3);
y= group y by $0;

--dump y 
z= foreach y generate group, COUNT(y);

STORE z INTO 'output' USING PigStorage (',');
fs -get output/ .