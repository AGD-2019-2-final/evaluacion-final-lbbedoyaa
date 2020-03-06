-- 
-- Pregunta
-- ===========================================================================
-- 
-- Para el archivo `data.tsv` compute Calcule la cantidad de registros en que 
-- aparece cada letra minúscula en la columna 2.
-- 
-- Escriba el resultado a la carpeta `output` del directorio actual.
-- 
fs -rm -f -r output;
--
-- >>> Escriba su respuesta a partir de este punto <<<



BD = LOAD 'data.tsv'
    AS (letra:CHARARRAY, minusculas: BAG{t: TUPLE(p:CHARARRAY)},MAP []);
BD = FOREACH BD GENERATE minusculas.p;

BD = FOREACH BD GENERATE FLATTEN ($0)  as minuscula;
grouped = group BD by minuscula;

wordcount = FOREACH grouped GENERATE group , COUNT(BD);

--wordcount = FOREACH grouped GENERATE $0 , COUNT($1);


STORE wordcount INTO 'output';
fs -get output/ .


       