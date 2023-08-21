DROP TABLE IF EXISTS persons;

CREATE TABLE persons (
  id SERIAL,
  first_name VARCHAR(50),
  last_name VARCHAR(50),
  dob DATE,
  email VARCHAR(255),
  PRIMARY KEY (id)
);

COPY persons(first_name, last_name, dob, email)
FROM '/docker-entrypoint-initdb.d/sample-data.csv'
DELIMITER ','
CSV HEADER;