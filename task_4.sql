-- ANALYZE SELECT *
-- FROM books

SELECT column_name, data_type 
FROM INFORMATION_SCHEMA.COLUMNS 
where table_name = 'columns'
  and table_schema = 'information_schema';