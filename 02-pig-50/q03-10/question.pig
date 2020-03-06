-- Pregunta
-- ===========================================================================
-- 
-- Obtenga los cinco (5) valores más pequeños de la 3ra columna.
-- Escriba el resultado a la carpeta `output` del directorio actual.
-- 
fs -rm -f -r output;
--
-- >>> Escriba su respuesta a partir de este punto <<<
--
--fs -rm -f -r data.tsv;
--fs -put data.tsv;

u = LOAD 'data.tsv' USING PigStorage ('\t')
    AS (letra:CHARARRAY, 
       fecha:CHARARRAY, 
       valor:INT);
       

--DUMP u;

y = ORDER u BY valor;

z= limit (foreach y generate $2) 5;

STORE z INTO 'output';
fs -get output/ .

--dump z;

--aa= limit z 5;
--dump aa