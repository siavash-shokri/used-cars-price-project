CREATE TABLE used_cars (
id BIGSERIAL NOT NULL PRIMARY KEY,
brand VARCHAR(50),
model VARCHAR(150),
model_year INTEGER,
milage VARCHAR(50),
fuel_type VARCHAR(50),
engine VARCHAR(150),
transmission VARCHAR(50),
ext_col VARCHAR(50),
int_col VARCHAR(50),
accident VARCHAR(100),
clean_title VARCHAR(20),
price VARCHAR(50));

\copy used_cars(brand, model, model_year, milage, fuel_type, engine, transmission, ext_col, int_col, accident, clean_title, price)
FROM '/home/fruckman/DataAnalysis/used_cars.csv'
DELIMITER ',' CSV HEADER;
ERROR:  value too long for type character varying(50)
CONTEXT:  COPY used_cars, line 765, column transmission: "Automatic, 8-Spd M STEPTRONIC w/Drivelogic, Sport & Manual Modes"

test=> ALTER TABLE used_cars
ALTER COLUMN brand TYPE TEXT,
ALTER COLUMN model TYPE TEXT,
ALTER COLUMN model_year TYPE TEXT,
ALTER COLUMN milage TYPE TEXT,
ALTER COLUMN fuel_type TYPE TEXT,
ALTER COLUMN engine TYPE TEXT,
ALTER COLUMN transmission TYPE TEXT,
ALTER COLUMN ext_col TYPE TEXT,
ALTER COLUMN int_col TYPE TEXT,
ALTER COLUMN accident TYPE TEXT,
ALTER COLUMN clean_title TYPE TEXT,
ALTER COLUMN price TYPE TEXT;

\copy used_cars(brand, model, model_year, milage, fuel_type, engine, transmission, ext_col, int_col, accident, clean_title, price)
FROM '/home/fruckman/DataAnalysis/used_cars.csv'
DELIMITER ',' CSV HEADER;

SELECT COUNT(*) FROM used_cars;

SELECT COUNT(DISTINCT brand) FROM used_cars;

SELECT COUNT(*) FROM used_cars WHERE fuel_type IS NULL;



