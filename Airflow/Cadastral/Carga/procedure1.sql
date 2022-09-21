CREATE OR REPLACE PROCEDURE display_message (INOUT msg TEXT)

 AS $$

 BEGIN

 RAISE NOTICE 'Procedure Parameter: %', msg ;

 END ;