# Keys and superkeys
/*What is a key?
Attribute(s) that identify a record uniquely
As long as attributes can be removed: superkey
If no more attributes can be removed: minimal superkey or key*/
/*Get to know SELECT COUNT DISTINCT
Your database doesn't have any defined keys so far, and you don't know which columns or combinations of columns are suited as keys.
There's a simple way of finding out whether a certain column (or a combination) contains only unique values – and thus identifies the records in the table.
You already know the SELECT DISTINCT query from the first chapter. Now you just have to wrap everything within the COUNT() function and PostgreSQL will return the number of unique rows for the given columns:
SELECT COUNT(DISTINCT(column_a, column_b, ...))
FROM table;*/

-- Count the number of distinct values in the university_city column
SELECT COUNT(DISTINCT(university_city)) 
FROM universities;

/*Identify keys with SELECT COUNT DISTINCT
There's a very basic way of finding out what qualifies for a key in an existing, populated table:
Count the distinct records for all possible combinations of columns. If the resulting number x equals the number of all rows in the table for a combination, you have discovered a superkey.
Then remove one column after another until you can no longer remove columns without seeing the number x decrease. If that is the case, you have discovered a (candidate) key.
The table professors has 551 rows. It has only one possible candidate key, which is a combination of two attributes. You might want to try different combinations using the "Run code" button. Once you have found the solution, you can submit your answer.*/
-- Try out different combinations
SELECT COUNT(DISTINCT(lastname,firstname)) 
FROM professors;

/*Indeed, the only combination that uniquely identifies professors is {firstname, lastname}. {firstname, lastname, university_shortname} is a superkey, and all other combinations give duplicate values. Hopefully, the concept of superkeys and keys is now a bit more clear. Let's move on to primary keys!*/

/*ADD key CONSTRAINTs to the tables
Two of the tables in your database already have well-suited candidate keys consisting of one column each: organizations and universities with the organization and university_shortname columns, respectively.
In this exercise, you'll specify primary key constraints for these columns and rename them to id.
Adding primary key constraints is as straightforward as adding unique constraints (see the last exercise of Chapter 2):
ALTER TABLE table_name
ADD CONSTRAINT some_name PRIMARY KEY (column_name)
Note that you can also specify more than one column in the brackets.*/
-- Rename the organization column to id
ALTER TABLE organizations
RENAME COLUMN organization TO id;

-- Make id a primary key
ALTER TABLE organizations
ADD CONSTRAINT organization_pk PRIMARY KEY (id);

-- Rename the university_shortname column to id
ALTER TABLE universities
RENAME COLUMN university_shortname TO id;

-- Make id a primary key
ALTER TABLE universities
ADD CONSTRAINT university_pk PRIMARY KEY(id);

# Surrogate keys
/*Add a SERIAL surrogate key
Since there's no single column candidate key in professors (only a composite key candidate consisting of firstname, lastname), you'll add a new column id to that table.
This column has a special data type serial, which turns the column into an auto-incrementing number. This means that, whenever you add a new professor to the table, it will automatically get an id that does not exist yet in the table: a perfect primary key!*/
-- Add the new column to the table
ALTER TABLE professors 
ADD COLUMN id serial PRIMARY KEY;

-- Add the new column to the table
ALTER TABLE professors 
ADD COLUMN id serial;

-- Make id a primary key
ALTER TABLE professors 
ADD CONSTRAINT professors_pkey PRIMARY KEY(id);

-- Add the new column to the table
ALTER TABLE professors 
ADD COLUMN id serial;

-- Make id a primary key
ALTER TABLE professors 
ADD CONSTRAINT professors_pkey PRIMARY KEY (id);

-- Have a look at the first 10 rows of professors
SELECT * FROM professors LIMIT 10;

/*CONCATenate columns to a surrogate key
Another strategy to add a surrogate key to an existing table is to concatenate existing columns with the CONCAT() function.
Let's think of the following example table:
CREATE TABLE cars (
 make varchar(64) NOT NULL,
 model varchar(64) NOT NULL,
 mpg integer NOT NULL
)
The table is populated with 10 rows of completely fictional data.
Unfortunately, the table doesn't have a primary key yet. None of the columns consists of only unique values, so some columns can be combined to form a key.
In the course of the following exercises, you will combine make and model into such a surrogate key.*/
-- Count the number of distinct rows with columns make, model
SELECT COUNT(DISTINCT(make, model)) 
FROM cars;

-- Add the id column
ALTER TABLE cars
ADD COLUMN id varchar(128);

-- Update id with make + model
UPDATE cars
SET id = CONCAT(make, model);

-- Make id a primary key
ALTER TABLE cars
ADD CONSTRAINT id_pk PRIMARY KEY(id);

-- Have a look at the table
SELECT * FROM cars;

-- Create the table
CREATE TABLE students (
  last_name varchar(128) NOT NULL,
  ssn integer PRIMARY KEY NOT NULL,
  phone_no char(12)
);