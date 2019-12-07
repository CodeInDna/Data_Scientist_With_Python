/*SELECT DISTINCT
Often your results will include many duplicate values. If you want to select all the unique values from a column, you can use the DISTINCT keyword.
This might be useful if, for example, you're interested in knowing which languages are represented in the films table:
SELECT DISTINCT language
FROM films;
Remember, you can check out the data in the tables by clicking on the tabs to the right under the editor!*/
SELECT DISTINCT country FROM films;

SELECT DISTINCT certification FROM films;

/*Practice with COUNT
As you've seen, COUNT(*) tells you how many rows are in a table. However, if you want to count the number of non-missing values in a particular column, you can call COUNT on just that column.
For example, to count the number of birth dates present in the people table:
SELECT COUNT(birthdate)
FROM people;
It's also common to combine COUNT with DISTINCT to count the number of distinct values in a column.
For example, this query counts the number of distinct birth dates contained in the people table:
SELECT COUNT(DISTINCT birthdate)
FROM people;
Let's get some practice with COUNT!*/

/*WHERE IN
As you've seen, WHERE is very useful for filtering results. However, if you want to filter based on many conditions, WHERE can get unwieldy. For example:
SELECT name
FROM kids
WHERE age = 2
OR age = 4
OR age = 6
OR age = 8
OR age = 10;
Enter the IN operator! The IN operator allows you to specify multiple values in a WHERE clause, making it easier and quicker to specify multiple OR conditions! Neat, right?
So, the above example would become simply:
SELECT name
FROM kids
WHERE age IN (2, 4, 6, 8, 10);
Try using the IN operator yourself!*/

SELECT title, language FROM films WHERE language IN ('English','Spanish','French');

/*Introduction to NULL and IS NULL
In SQL, NULL represents a missing or unknown value. You can check for NULL values using the expression IS NULL. For example, to count the number of missing birth dates in the people table:
SELECT COUNT(*)
FROM people
WHERE birthdate IS NULL;
As you can see, IS NULL is useful when combined with WHERE to figure out what data you're missing.
Sometimes, you'll want to filter out missing values so you only get results which are not NULL. To do this, you can use the IS NOT NULL operator.
For example, this query gives the names of all people whose birth dates are not missing in the people table.
SELECT name
FROM people
WHERE birthdate IS NOT NULL;*/

SELECT COUNT(*) FROM films WHERE language IS NULL;

/*LIKE and NOT LIKE
As you've seen, the WHERE clause can be used to filter text data. However, so far you've only been able to filter by specifying the exact text you're interested in. In the real world, often you'll want to search for a pattern rather than a specific text string.
In SQL, the LIKE operator can be used in a WHERE clause to search for a pattern in a column. To accomplish this, you use something called a wildcard as a placeholder for some other values. There are two wildcards you can use with LIKE:
The % wildcard will match zero, one, or many characters in text. For example, the following query matches companies like 'Data', 'DataC' 'DataCamp', 'DataMind', and so on:
SELECT name
FROM companies
WHERE name LIKE 'Data%';
The _ wildcard will match a single character. For example, the following query matches companies like 'DataCamp', 'DataComp', and so on:
SELECT name
FROM companies
WHERE name LIKE 'DataC_mp';
You can also use the NOT LIKE operator to find records that don't match the pattern you specify.
Got it? Let's practice!*/

SELECT name FROM people WHERE name LIKE 'B%';

SELECT name FROM people WHERE name LIKE 'B%';