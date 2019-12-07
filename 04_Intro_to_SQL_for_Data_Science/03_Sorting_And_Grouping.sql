/*ORDER BY
Congratulations on making it this far! You now know how to select and filter your results.
In this chapter you'll learn how to sort and group your results to gain further insight. Let's go!
In SQL, the ORDER BY keyword is used to sort results in ascending or descending order according to the values of one or more columns.
By default ORDER BY will sort in ascending order. If you want to sort the results in descending order, you can use the DESC keyword. For example,
SELECT title
FROM films
ORDER BY release_year DESC;
gives you the titles of films sorted by release year, from newest to oldest.
How do you think ORDER BY sorts a column of text values by default?*/


/*Sorting multiple columns
ORDER BY can also be used to sort on multiple columns. It will sort by the first column specified, then sort by the next, then the next, and so on. For example,
SELECT birthdate, name
FROM people
ORDER BY birthdate, name;
sorts on birth dates first (oldest to newest) and then sorts on the names in alphabetical order. The order of columns is important!
Try using ORDER BY to sort multiple columns! Remember, to specify multiple columns you separate the column names with a comma.*/

/*GROUP BY
Now you know how to sort results! Often you'll need to aggregate results. For example, you might want to count the number of male and female employees in your company. Here, what you want is to group all the males together and count them, and group all the females together and count them. In SQL, GROUP BY allows you to group a result by one or more columns, like so:
SELECT sex, count(*)
FROM employees
GROUP BY sex;
This might give, for example:
sex	count
male	15
female	19
Commonly, GROUP BY is used with aggregate functions like COUNT() or MAX(). Note that GROUP BY always goes after the FROM clause!*/

SELECT release_year,country,MAX(budget) FROM films GROUP BY release_year, country ORDER BY release_year, country;

/*HAVING a great time
In SQL, aggregate functions can't be used in WHERE clauses. For example, the following query is invalid:
SELECT release_year
FROM films
GROUP BY release_year
WHERE COUNT(title) > 10;
This means that if you want to filter based on the result of an aggregate function, you need another way! That's where the HAVING clause comes in. For example,
SELECT release_year
FROM films
GROUP BY release_year
HAVING COUNT(title) > 10;
shows only those years in which more than 10 films were released.
In how many different years were more than 200 movies released?*/

-- select country, average budget, average gross
SELECT country, AVG(budget) AS avg_budget, AVG(gross) AS avg_gross
-- from the films table
FROM films
-- group by country 
GROUP BY country
-- where the country has more than 10 titles
HAVING COUNT(title) > 10
-- order by country
ORDER BY country
-- limit to only show 5 results
LIMIT 5;

SELECT title, imdb_score
FROM films
JOIN reviews
ON films.id = reviews.film_id
WHERE title = 'To Kill a Mockingbird';