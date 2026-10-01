-- Used Cars Market Analysis
-- PostgreSQL data loading, cleaning, and exploratory analysis


-- ============================================================
-- 1. Load and Prepare Data
-- ============================================================

DROP TABLE IF EXISTS used_cars;

CREATE TABLE used_cars (
id BIGSERIAL NOT NULL PRIMARY KEY,
brand TEXT,
model TEXT,
model_year TEXT,
milage TEXT,
fuel_type TEXT,
engine TEXT,
transmission TEXT,
ext_col TEXT,
int_col TEXT,
accident TEXT,
clean_title TEXT,
price TEXT);

\copy used_cars(brand, model, model_year, milage, fuel_type, engine, transmission, ext_col, int_col, accident, clean_title, price) FROM '/home/fruckman/DataAnalysis/used-cars-price-project/data/used_cars.csv' DELIMITER ',' CSV HEADER;

ALTER TABLE used_cars 
ALTER COLUMN price TYPE NUMERIC 
USING NULLIF(REPLACE(REPLACE(TRIM(price), '$', ''), ',', ''), '')::NUMERIC;

ALTER TABLE used_cars 
ALTER COLUMN milage TYPE INTEGER 
USING NULLIF(REPLACE(REPLACE(TRIM(milage), 'mi.', ''), ',', ''), '')::INTEGER;

ALTER TABLE used_cars 
ALTER COLUMN model_year TYPE INTEGER USING model_year::INTEGER;


-- ============================================================
-- 2. Basic Dataset Checks
-- ============================================================

SELECT COUNT(*) FROM used_cars;

SELECT MIN(model_year), MAX(model_year) 
FROM used_cars;


-- ============================================================
-- 3. Frequency Analysis
-- ============================================================

SELECT brand, COUNT(id) AS cnt 
FROM used_cars 
GROUP BY brand 
ORDER BY cnt DESC
FETCH FIRST 10 ROWS ONLY;

SELECT model, COUNT(id) AS cnt 
FROM used_cars 
GROUP BY model 
ORDER BY cnt DESC
FETCH FIRST 10 ROWS ONLY;


-- ============================================================
-- 4. Market Price Analysis
-- ============================================================

SELECT brand, 
percentile_cont(0.5) WITHIN GROUP (ORDER BY price) AS median_price 
FROM used_cars 
GROUP BY brand 
ORDER BY median_price DESC;

SELECT fuel_type, 
percentile_cont(0.5) WITHIN GROUP (ORDER BY price) AS median_price 
FROM used_cars 
GROUP BY fuel_type 
ORDER BY median_price DESC;

SELECT accident, 
percentile_cont(0.5) WITHIN GROUP (ORDER BY price) AS median_price 
FROM used_cars 
GROUP BY accident 
ORDER BY median_price DESC;

SELECT model_year, 
percentile_cont(0.5) WITHIN GROUP (ORDER BY price) AS median_price 
FROM used_cars 
GROUP BY model_year 
ORDER BY median_price DESC;


-- ============================================================
-- 5. Mileage Analysis
-- ============================================================

SELECT brand, 
AVG(milage) AS avg_milage
FROM used_cars 
GROUP BY brand 
ORDER BY avg_milage DESC;


-- ============================================================
-- 6. Missing Value Check
-- ============================================================

SELECT
    COUNT(*) FILTER (WHERE fuel_type IS NULL) AS missing_fuel_type,
    COUNT(*) FILTER (WHERE accident IS NULL) AS missing_accident,
    COUNT(*) FILTER (WHERE clean_title IS NULL) AS missing_clean_title
FROM used_cars;