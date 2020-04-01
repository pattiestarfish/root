-- This is the first query:

SELECT DISTINCT year from population_years;

-- Add your additional queries below:

SELECT population, year FROM population_years
WHERE country = 'Gabon'
ORDER BY population DESC
LIMIT 1;

SELECT country, population FROM population_years
WHERE year = 2005
ORDER BY population ASC
LIMIT 10;

SELECT DISTINCT country, population FROM population_years
WHERE population > 100.0
  AND year = 2010
  ORDER BY population DESC;

SELECT DISTINCT country FROM population_years
WHERE country LIKE '%Islands%';

SELECT country, population, year FROM population_years
WHERE country = 'Indonesia'
  AND year BETWEEN 2000 AND 2010
  ORDER BY year DESC;