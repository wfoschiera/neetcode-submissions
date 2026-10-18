CREATE TABLE stocks (
  id INTEGER PRIMARY KEY,
  name TEXT,
  transaction_dates DATE[]
);

-- Do not modify above this line --
INSERT INTO stocks (id, name, transaction_dates)
    VALUES (1, 'AAPL', ARRAY[DATE('2007-02-09'), DATE('2007-02-10'), DATE('2007-02-11')]), (2, 'GOOG', ARRAY[DATE('2004-12-15'), DATE('2004-12-16')]);


-- Do not modify below this line --
SELECT * FROM stocks;
