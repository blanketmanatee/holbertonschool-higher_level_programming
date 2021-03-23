-- lists all the cities in CA found in hbtn_0d_usa
-- results sorted into ascending order cities.id

SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY id;